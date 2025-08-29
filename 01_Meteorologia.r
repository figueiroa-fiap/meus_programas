# Instalar pacotes se necessário
# install.packages("httr")
# install.packages("jsonlite")

library(httr)
library(jsonlite)

cidade <- readline(prompt = "Digite o nome de uma cidade: ")

# Função para buscar informações do clima pela cidade
get_weather_info <- function(city, api_key) {
  base_url <- "https://api.openweathermap.org/data/2.5/weather"
  
  # Requisição à API
  response <- GET(base_url, query = list(
    q = city,
    appid = api_key,
    units = "metric",  # Celsius
    lang = "pt"        # Português
  ))
  
  # Verifica se deu certo
  if (status_code(response) != 200) {
    stop("Erro ao acessar a API: ", content(response, "text"))
  }
  
  # Converte para JSON
  data <- fromJSON(content(response, "text", encoding = "UTF-8"))
  
  # Extrai informações
  result <- list(
    pais = data$sys$country,
    cidade = data$name,
    temperatura = data$main$temp,
    sensacao_termica = data$main$feels_like,
    vento_velocidade = data$wind$speed
  )
  
  return(result)
}

# ========================
# Exemplo de uso:
# ========================

# Substitua pela sua chave da API do OpenWeatherMap
api_key <- "6f3850cb9fe570f99c0da937bd690558"

info <- get_weather_info(cidade, api_key)

cat("\n--- INFORMAÇÕES DO CLIMA ---\n")
cat("📍 Cidade: ", info$cidade, " - ", info$pais, "\n")
cat("🌡️ Temperatura: ", info$temperatura, "°C\n")
cat("🤔 Sensação Térmica do momento: ", info$sensacao_termica, "°C\n")
cat("💨 Velocidade do Vento: ", info$vento_velocidade, " m/s\n")
