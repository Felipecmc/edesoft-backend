# edesoft-backend

Para rodar o serviço basta seguir os seguintes passos

- na raiz do projeto criar o ambiente virtual com python -m venv venv

- instalar as dependências com pip install -r requirements.txt

- criar migrations com python manage.py makemigrations

-criar o banco sqlite3 com python manage.py migrate (o banco foi escolhido justamente pela facilidade de ser testado e criado sem maiores problemas para avaliação)

- rodar o servidor com python manage.py runserver

# Pronto agora o serviço está de pé

-na rota /api/csv/ deve ser feito um post com os argumentos "bucket_name" e "object_key" para fazer a leitura e tratamento de arquivos csv que tenham o padrão do exemplo fornecido

-na rota /api/local-csv/ deve ser feito um post para ler e tratar arquivos locais que tenham o mesmo padrão do exemplo fornecido

#Disclaimer

- para melhor visualização do banco baixe a extensão SQLite Viewer

-O banco db.sqlite3 não se recarrega automaticamente após uma requisição, então se ele já estiver aberto em sua IDE recomendo que feche o arquivo e abra de novo
