import psutil
import time

class Host:
    def __init__(self):
        self.dados_rede = None
        self.bytes_enviados = 0
        self.bytes_recebidos = 0

    def obter_dados_rede(self):
        self.dados_rede = psutil.net_io_counters()
        self.bytes_enviados = self.dados_rede.bytes_sent
        self.bytes_recebidos = self.dados_rede.bytes_recv
        return self.bytes_enviados, self.bytes_recebidos

    def converter_bytes_para_gb(self, bytes_valor):

        return bytes_valor / (1024 ** 3)

    def monitorar_banda_larga(self, intervalo_segundos=5, duracao_minutos=30):
        tempo_inicio = time.time()
        tempo_fim = tempo_inicio + (duracao_minutos * 60)

        print("Iniciando monitoramento de banda larga...")
        while time.time() < tempo_fim:
            bytes_enviados, bytes_recebidos = self.obter_dados_rede()


            print(f"Enviados: {self.converter_bytes_para_gb(bytes_enviados):.2f} GB | "
                  f"Recebidos: {self.converter_bytes_para_gb(bytes_recebidos):.2f} GB")

            time.sleep(intervalo_segundos)

        print("Monitoramento concluído.")

if __name__ == "__main__":
    host = Host()

    
    intervalo_segundos = 5
    duracao_minutos = 1 


    host.monitorar_banda_larga(intervalo_segundos, duracao_minutos)
