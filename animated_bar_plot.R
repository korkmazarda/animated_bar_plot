# Libraries:
library(ggplot2)
library(gganimate)

# Creating the monthly dataframes

x_06=data.frame(Product=c("A","B","C","D","E","F","G","H","J","K")
                    , Download=c(3059,3692,2524,1879,2100,2595,0,1613,665,1239)
                    , months=rep('201806',10))


x_07=data.frame(Product=c("A","B","C","D","E","F","G","H","J","K")
                    , Download=c(3872,3526,2666,2559,2618,2151,0,1726,1531,1599)
                    , months=rep('201807',10))

x_08=data.frame(Product=c("A","B","C","D","E","F","G","H","J","K")
                    , Download=c(4042,4000,2852,2178,2518,2207,0,2578,2805,1448)
                    , months=rep('201808',10))


x_09=data.frame(Product=c("A","B","C","D","E","F","G","H","J","K")
                    , Download=c(3286,3528,2481,2079,2088,2529,3418,1632,1984,1463)
                    , months=rep('201809',10))

x_10=data.frame(Product=c("A","B","C","D","E","F","G","H","J","K")
                    , Download=c(8490,6561,5687,5057,3758,3743,4281,3037,2578,2599)
                    , months=rep('201810',10))

# Bind them into one

x_bind=rbind(x_06,x_07,x_08,x_09,x_10)

# Creating the index values for our final dataframe

index <- rep(1:5,each=10)

# Creating the label values as char for geom_text 

downloads_x <- c(as.character(x_06$Download),
                      as.character(x_07$Download),
                      as.character(x_08$Download),
                      as.character(x_09$Download),
                      as.character(x_10$Download))

# Creating the final dataframe and rename the columns

df_x <- data.frame(index,x_bind[, 1],x_bind[, 2], x_bind[, 3],downloads_x)

names(df_x) <- c("Index", "Products", "Downloads", "Months","Values")

df_x

# Plot and Animate

a <- ggplot(df_x, aes(x = Products,y = Downloads, fill = Products)) +
  geom_bar(stat = "identity") +
  labs(title = "Month: {closest_state}") +
  geom_text(aes(label = Values, y = Downloads),
            position = position_dodge(0.9), vjust = -1 ) +
  theme_classic() +
  transition_states(states = Months, transition_length = 2, state_length = 1) + 
  enter_fade() + 
  exit_shrink() +
  ease_aes('sine-in-out')

a_gif <- animate(a, width = 940, height = 480)

a_gif
