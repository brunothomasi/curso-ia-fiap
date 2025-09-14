# farmtech.R
# install.packages("jsonlite")
# install.packages("rlang")
# ---------------------------
# Exemplo de dados simulados
# ---------------------------
# Lê o CSV que o Python atualizou

dados <- read.csv("dados.csv",
                  header = TRUE,
                  sep = ",",
                  fileEncoding = "UTF-8")


culturas <- dados$cultura
areas <- as.numeric(dados$area)
insumos <- as.numeric(dados$totalinsumo)


# ---------------------------
# Estatísticas básicas
# ---------------------------
cat("Média das áreas plantadas:", mean(areas, na.rm = TRUE), "\n")
cat("Desvio-padrão das áreas:", sd(areas, na.rm = TRUE), "\n")

cat("Média dos insumos:", mean(insumos, na.rm = TRUE), "\n")
cat("Desvio-padrão dos insumos:", sd(insumos, na.rm = TRUE), "\n")


# ---------------------------
# Consulta a API meteorológica
# ---------------------------
# install.packages("httr")
library(httr)
library(jsonlite)

# Exemplo com OpenWeatherMap (precisa de chave de API gratuita)
cidade <- "Sao Paulo"
api_key <- "3f31e968e6dd877bfba6500be2574b3a"

# url encoded
url <- paste0("https://api.openweathermap.org/data/2.5/weather?q=", 
              URLencode(cidade), "&appid=", api_key, "&units=metric&lang=pt")

cat("Consultando clima em", cidade, "...\n")
resposta <- GET(url)
previsao <- fromJSON(content(resposta, "text", encoding = "UTF-8"))

dataframe <- as.data.frame(previsao$weather)
clima <- dataframe$description

cat("Clima em", cidade, ":", clima, "\n")
cat("Temperatura:", previsao$main$temp, "°C\n")
cat("Umidade:", previsao$main$humidity, "%\n")