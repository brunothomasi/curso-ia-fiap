# farmtech.R
#install.packages("jsonlite")
#install.packages("rlang")
# ---------------------------
# Exemplo de dados simulados
# ---------------------------
# Lê o CSV que o Python atualizou
dados <- read.csv("c:/Users/Daniel/Desktop/MEUS PROJETOS/dados.csv",
                  header = TRUE,
                  sep = ",",
                  fileEncoding = "UTF-8")


culturas <- dados$cultura
areas <- as.numeric(dados$area)
insumos <- as.numeric(dados$insumo)



# ---------------------------
# Estatísticas básicas
# ---------------------------
cat("Média das áreas plantadas:", mean(areas, na.rm = TRUE), "\n")
cat("Desvio-padrão das áreas:", sd(areas, na.rm = TRUE), "\n")

cat("Média dos insumos:", mean(insumos, na.rm = TRUE), "\n")
cat("Desvio-padrão dos insumos:", sd(insumos, na.rm = TRUE), "\n")



# ---------------------------
# (Ir além) Consulta a API meteorológica
# ---------------------------
#library(httr)
#library(jsonlite)

# Exemplo com OpenWeatherMap (precisa de chave de API gratuita)
#cidade <- "Sao Paulo"
#api_key <- "SUA_CHAVE_API_AQUI"
#url <- paste0("https://api.openweathermap.org/data/2.5/weather?q=", 
              #cidade, "&appid=", api_key, "&units=metric&lang=pt")

#resposta <- GET(url)
#dados <- fromJSON(content(resposta, "text", encoding = "UTF-8"))

#cat("Clima em", cidade, ":", dados$weather[[1]]$description, "\n")
#cat("Temperatura:", dados$main$temp, "°C\n")
#cat("Umidade:", dados$main$humidity, "%\n")

print(culturas)