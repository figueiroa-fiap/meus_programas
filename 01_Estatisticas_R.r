# =========================================================
# Estatísticas da Fazenda - Análise por Cultura
# =========================================================

library(dplyr)
library(ggplot2)

# ---------------------------------------------------------
# Caminhos
# ---------------------------------------------------------
arquivo_csv <- "C:/Users/rfigu/Desktop/dados_fazenda.csv"
pasta_graficos <- "C:/Users/rfigu/Desktop/Imagens/"
arquivo_estatisticas <- "C:/Users/rfigu/Desktop/dados_fazenda_estatisticas.csv"

# ---------------------------------------------------------
# Ler os dados
# ---------------------------------------------------------
dados <- read.csv(arquivo_csv, stringsAsFactors = FALSE)
dados$Área <- as.numeric(dados$Área)

# ---------------------------------------------------------
# Estatísticas agrupadas por Cultura
# ---------------------------------------------------------
estatisticas_por_cultura <- dados %>%
  group_by(Cultura) %>%
  summarise(
    count = n(),
    media_area = mean(Área),
    mediana_area = median(Área),
    sd_area = sd(Área),
    min_area = min(Área),
    max_area = max(Área),
    amplitude = max_area - min_area,
    coef_var = sd_area / media_area
  )

# Mostrar resultados
print(estatisticas_por_cultura)

# Salvar estatísticas em CSV
write.csv(estatisticas_por_cultura, arquivo_estatisticas, row.names = FALSE)
cat("Estatísticas salvas em CSV:", arquivo_estatisticas, "\n")

# ---------------------------------------------------------
# Gráficos
# ---------------------------------------------------------

# Histograma
grafico_hist <- ggplot(dados, aes(x = Área, fill = Cultura)) +
  geom_histogram(binwidth = 50, alpha = 0.7, position = "dodge") +
  labs(title = "Histograma da Área por Cultura",
       x = "Área (m²)",
       y = "Frequência") +
  theme_minimal()

# Boxplot
grafico_box <- ggplot(dados, aes(x = Cultura, y = Área, fill = Cultura)) +
  geom_boxplot(alpha = 0.7) +
  labs(title = "Boxplot da Área por Cultura",
       x = "Cultura",
       y = "Área (m²)") +
  theme_minimal()

# Densidade
grafico_dens <- ggplot(dados, aes(x = Área, color = Cultura, fill = Cultura)) +
  geom_density(alpha = 0.3) +
  labs(title = "Densidade da Área por Cultura",
       x = "Área (m²)",
       y = "Densidade") +
  theme_minimal()

# ---------------------------------------------------------
# Salvar gráficos em PNG
# ---------------------------------------------------------
png(filename = paste0(pasta_graficos, "histograma_area_por_cultura.png"), width = 800, height = 600)
print(grafico_hist)
dev.off()

png(filename = paste0(pasta_graficos, "boxplot_area_por_cultura.png"), width = 800, height = 600)
print(grafico_box)
dev.off()

png(filename = paste0(pasta_graficos, "densidade_area_por_cultura.png"), width = 800, height = 600)
print(grafico_dens)
dev.off()

cat("Gráficos salvos na pasta:", pasta_graficos, "\n")



