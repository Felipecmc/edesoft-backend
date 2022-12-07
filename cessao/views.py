from rest_framework.views import APIView, Response, Request, status
from .utils import readCSV
from .serializers import CessaoSerializer
import ipdb

class ReadCSVView(APIView):
    def post(self, request:Request):
        #ipdb.set_trace()
        data = readCSV(request.data)
        
        objects = []
        
        for row in data:
            if row[0] != "Originador":
               object = {
                "originador": row[0],
                "doc_originador": row[1],
                "doc_cedente": row[2],
                "cedente": row[3],
                "ccb": row[4],
                "id_cessao": row[5],
                "cliente": row[6],
                "cpf_cnpj": row[7],
                "endereco": row[8],
                "cep": row[9],
                "cidade": row[10],
                "uf": row[11],
                "valor_do_emprestimo": row[12],
                "valor_parcela": row[14],
                "total_parcelas": row[19],
                "parcela": row[20],
                "data_de_emissao":row[23],
                "data_de_vencimento": row[24],
                "preco_de_aquisicao": row[26]
                }
               
            serializer = CessaoSerializer(data = object)
            serializer.is_valid(raise_exception=True)
            objects.append(serializer)
            serializer.save()
            
        return Response(objects, status.HTTP_200_OK)
            

