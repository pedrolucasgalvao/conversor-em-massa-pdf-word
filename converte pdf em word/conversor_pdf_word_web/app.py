import os
import zipfile
from flask import Flask, render_template, request, redirect, url_for, send_file
from pdf2docx import Converter

# Configura o Flask
app = Flask(__name__)

# Configura as pastas de upload e conversão
UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(CONVERTED_FOLDER):
    os.makedirs(CONVERTED_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONVERTED_FOLDER'] = CONVERTED_FOLDER

@app.route('/')
def index():
    """Rota para a página inicial, onde o usuário fará o upload dos arquivos."""
    return render_template('index.html')

@app.route('/converter', methods=['POST'])
def converter_arquivos():
    """Rota para processar os arquivos e fazer a conversão."""
    
    arquivos = request.files.getlist('arquivos_pdf')
    arquivos_convertidos = []
    
    if not arquivos or arquivos[0].filename == '':
        return redirect(url_for('index'))

    for arquivo_pdf in arquivos:
        if arquivo_pdf and arquivo_pdf.filename.endswith('.pdf'):
            # Salva o arquivo PDF
            caminho_pdf = os.path.join(app.config['UPLOAD_FOLDER'], arquivo_pdf.filename)
            arquivo_pdf.save(caminho_pdf)
            
            # Converte o PDF para DOCX
            try:
                nome_base = os.path.splitext(arquivo_pdf.filename)[0]
                caminho_docx = os.path.join(app.config['CONVERTED_FOLDER'], f"{nome_base}.docx")
                
                cv = Converter(caminho_pdf)
                cv.convert(caminho_docx)
                cv.close()
                
                arquivos_convertidos.append(caminho_docx)
            except Exception as e:
                print(f"Erro ao converter {arquivo_pdf.filename}: {e}")
                # Aqui você pode adicionar uma mensagem de erro na página se quiser
    
    if arquivos_convertidos:
        # Cria um arquivo ZIP para agrupar os arquivos convertidos
        zip_nome = 'arquivos_convertidos.zip'
        caminho_zip = os.path.join(app.config['CONVERTED_FOLDER'], zip_nome)
        
        with zipfile.ZipFile(caminho_zip, 'w') as zip_file:
            for arq_convertido in arquivos_convertidos:
                # Adiciona o arquivo ao ZIP
                zip_file.write(arq_convertido, os.path.basename(arq_convertido))
        
        return render_template('resultado.html', zip_filename=zip_nome)
    
    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_arquivo(filename):
    """Rota para o usuário fazer o download do arquivo ZIP."""
    caminho_arquivo = os.path.join(app.config['CONVERTED_FOLDER'], filename)
    return send_file(caminho_arquivo, as_attachment=True)

if __name__ == '__main__':
    # Roda o servidor web em modo de desenvolvimento
    app.run(debug=True)