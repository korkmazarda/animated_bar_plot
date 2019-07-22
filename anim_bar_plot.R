install.packages("ggplot2")
install.packages("gganimate")

library(readr)
library(gganimate)

df_r_usa <- read_csv("./df_usa_merged.csv")


staticplot = ggplot(df_r_usa, aes(index, group = Title, 
                                   fill = as.factor(Title), color = as.factor(Title))) +
  geom_tile(aes(y = Streams/2,
                height = Streams,
                width = 0.9), alpha = 0.8, color = NA) +
  geom_text(aes(y = 0, label = paste(Title, " ")), vjust = 0.2, hjust = 1) +
  geom_text(aes(y=Streams,label = Streams, hjust=0)) +
  coord_flip(clip = "off", expand = FALSE) +
  scale_y_continuous(labels = scales::comma) +
  scale_x_reverse() +
  guides(color = FALSE, fill = FALSE) +
  theme(axis.line=element_blank(),
        axis.text.x=element_blank(),
        axis.text.y=element_blank(),
        axis.ticks=element_blank(),
        axis.title.x=element_blank(),
        axis.title.y=element_blank(),
        legend.position="none",
        panel.background=element_rect(colour = "lightcyan1"),
        panel.border=element_blank(),
        panel.grid.major=element_blank(),
        panel.grid.minor=element_blank(),
        panel.grid.major.x = element_line( size=.1, color="grey" ),
        panel.grid.minor.x = element_line( size=.1, color="grey" ),
        plot.title=element_text(size=25, hjust=0.5, face="bold", colour="grey", vjust=-1),
        plot.subtitle=element_text(size=18, hjust=0.5, face="italic", color="grey"),
        plot.caption =element_text(size=12, hjust=0.5, face="italic", color="grey"),
        plot.background=element_blank(),
        plot.margin = margin(2 ,8, 2, 4, "cm"))



anim = staticplot + transition_states(YearMonth, transition_length = 4, state_length = 1) +
  view_follow(fixed_x = TRUE)  +
  labs(title = 'Year_Month : {closest_state}',  
       subtitle  =  "Top 10 Titles (USA)",
       caption  = "Top 10 USA Titles by their streamings")


install.packages("gifski_renderer")

animate(anim, 400, fps = 20,  width = 1200, height = 800, 
        renderer = gifski_renderer("spotify_usa.gif"))


