from datetime import datetime, timedelta


class Datas:
    def __init__(self):
        self.data_cadastro = datetime.today()

    def mes_cadastro(self):
        lista_meses = [
            'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
        ]

        mes = self.data_cadastro.month - 1
        return lista_meses[mes]

    def __str__(self):
        return self.formata_data()

    def dia_semana(self):
        lista_semana = [
            'Segunda', 'Terça', 'Quarta', 'Quinta',
            'Sexta', 'Sábado', 'Domingo'
        ]

        dia = self.data_cadastro.weekday()
        return lista_semana[dia] + '-feira'

    def formata_data(self):
        formatado = self.data_cadastro.strftime('%d/%m/%Y %H:%M')
        return formatado

    def tempo_cadastro(self):
        return datetime.today() - self.data_cadastro
