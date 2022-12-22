#1. 외식업 연매출 TOP10 상권
totalTOP10 <- read.csv("Machine_visual/totalTOP10.csv")
totalTOP10

library(ggplot2)

totalTOP10<-totalTOP10[,1:2]

tf = function(num){
  tf_num = function(x){
    new_num = x%/% 100000000
    return(paste(new_num, '억', sep = ''))
  }
  return(sapply(num, tf_num))
}

ggplot(totalTOP10,aes(x = 외식업_연매출_금액, y = reorder(상권_코드_명,-외식업_연매출_금액), fill=상권_코드_명))+
  geom_bar(stat='identity') +
  ggtitle('외식업 연매출 TOP10 상권')+
  theme(plot.title = element_text(size=25, face='bold', hjust = 0.5))+
  labs(x="연매출금액",y = "상권")+
  scale_x_continuous(limits=c(0,6000000000),labels = tf)+
  theme(legend.position = "none")

ggsave("Machine_visual/totalTOP10.png")

#2. 한식음식점 연매출 TOP10 상권
Koreanfood <- read.csv("Machine_visual/Koreanfood.csv")

Koreanfood_revenue<-Koreanfood[,1:2]
names(Koreanfood_revenue)[2] <- c('한식음식점_연매출_금액')

ggplot(Koreanfood_revenue,aes(x = 한식음식점_연매출_금액, y = reorder(상권_코드_명,-한식음식점_연매출_금액), fill=상권_코드_명))+
  geom_bar(stat='identity') +
  ggtitle('한식음식점 연매출 TOP10 상권')+
  theme(plot.title = element_text(size=25, face='bold', hjust = 0.5))+
  labs(x="연매출금액",y = "상권")+
  scale_x_continuous(limits=c(0,1600000000),labels = tf)+
  theme(legend.position = "none")

ggsave("Machine_visual/Koreanfood.png")

#3. 중식음식점 연매출 TOP10 상권
Chinesefood <- read.csv("Machine_visual/Chinesefood.csv")

Chinesefood_revenue<-Chinesefood[,1:2]
names(Chinesefood_revenue)[2] <- c('중식음식점_연매출_금액')

ggplot(Chinesefood_revenue,aes(x = 중식음식점_연매출_금액, y = reorder(상권_코드_명,-중식음식점_연매출_금액), fill=상권_코드_명))+
  geom_bar(stat='identity') +
  ggtitle('중식음식점 연매출 TOP10 상권')+
  theme(plot.title = element_text(size=25, face='bold', hjust = 0.5))+
  labs(x="연매출금액",y = "상권")+
  scale_x_continuous(limits=c(0,3000000000),labels = tf)+
  theme(legend.position = "none")

ggsave("Machine_visual/Chinesefood.png")

#4. 일식점 연매출 TOP10 상권
Japanesefood <- read.csv("Machine_visual/Japanesefood.csv")

Japanesefood_revenue<-Japanesefood[,1:2]
names(Japanesefood_revenue)[2] <- c('일식음식점_연매출_금액')

ggplot(Japanesefood_revenue,aes(x = 일식음식점_연매출_금액, y = reorder(상권_코드_명,-일식음식점_연매출_금액), fill=상권_코드_명))+
  geom_bar(stat='identity') +
  ggtitle('일중식음식점 연매출 TOP10 상권')+
  theme(plot.title = element_text(size=25, face='bold', hjust = 0.5))+
  labs(x="연매출금액",y = "상권")+
  scale_x_continuous(limits=c(0,1600000000),labels = tf)+
  theme(legend.position = "none")

ggsave("Machine_visual/Japanesefood.png")

#5. 양식점 연매출 TOP10 상권
Westernfood <- read.csv("Machine_visual/Westernfood.csv")

Westernfood_revenue<-Westernfood[,1:2]
names(Westernfood_revenue)[2] <- c('양식음식점_연매출_금액')

ggplot(Westernfood_revenue,aes(x = 양식음식점_연매출_금액, y = reorder(상권_코드_명,-양식음식점_연매출_금액), fill=상권_코드_명))+
  geom_bar(stat='identity') +
  ggtitle('양식음식점 연매출 TOP10 상권')+
  theme(plot.title = element_text(size=25, face='bold', hjust = 0.5))+
  labs(x="연매출금액",y = "상권")+
  scale_x_continuous(limits=c(0,1100000000),labels = tf)+
  theme(legend.position = "none")

ggsave("Machine_visual/Westernfood.png")

#6. 제과점 연매출 TOP10 상권
Bakery <- read.csv("Machine_visual/Bakery.csv")

Bakery_revenue<-Bakery[,1:2]
names(Bakery_revenue)[2] <- c('제과점_연매출_금액')

ggplot(Bakery_revenue,aes(x = 제과점_연매출_금액, y = reorder(상권_코드_명,-제과점_연매출_금액), fill=상권_코드_명))+
  geom_bar(stat='identity') +
  ggtitle('제과점 연매출 TOP10 상권')+
  theme(plot.title = element_text(size=25, face='bold', hjust = 0.5))+
  labs(x="연매출금액",y = "상권")+
  scale_x_continuous(limits=c(0,2000000000),labels = tf)+
  theme(legend.position = "none")

ggsave("Machine_visual/Bakery.png")

#7. 패스트푸드점 연매출 TOP10 상권
Fast_food <- read.csv("Machine_visual/Fast_food.csv")

Fast_food_revenue<-Fast_food[,1:2]
names(Fast_food_revenue)[2] <- c('패스트푸드점_연매출_금액')

ggplot(Fast_food_revenue,aes(x = 패스트푸드점_연매출_금액, y = reorder(상권_코드_명,-패스트푸드점_연매출_금액), fill=상권_코드_명))+
  geom_bar(stat='identity') +
  ggtitle('패스트푸드점 연매출 TOP10 상권')+
  theme(plot.title = element_text(size=25, face='bold', hjust = 0.5))+
  labs(x="연매출금액",y = "상권")+
  scale_x_continuous(limits=c(0,2000000000),labels = tf)+
  theme(legend.position = "none")

ggsave("Machine_visual/Fast_food.png")

#8. 치킨전문점 연매출 TOP10 상권
Chicken <- read.csv("Machine_visual/Chicken.csv")

Chicken_revenue<-Chicken[,1:2]
names(Chicken_revenue)[2] <- c('치킨전문점_연매출_금액')

ggplot(Chicken_revenue,aes(x = 치킨전문점_연매출_금액, y = reorder(상권_코드_명,-치킨전문점_연매출_금액), fill=상권_코드_명))+
  geom_bar(stat='identity') +
  ggtitle('치킨전문점 연매출 TOP10 상권')+
  theme(plot.title = element_text(size=25, face='bold', hjust = 0.5))+
  labs(x="연매출금액",y = "상권")+
  scale_x_continuous(limits=c(0,2000000000),labels = tf)+
  theme(legend.position = "none")

ggsave("Machine_visual/Chicken.png")

#9. 분식전문점 연매출 TOP10 상권
Snackbar <- read.csv("Machine_visual/Snackbar.csv")

Snackbar_revenue<-Snackbar[,1:2]
names(Snackbar_revenue)[2] <- c('분식전문점_연매출_금액')

ggplot(Snackbar_revenue,aes(x = 분식전문점_연매출_금액, y = reorder(상권_코드_명,-분식전문점_연매출_금액), fill=상권_코드_명))+
  geom_bar(stat='identity') +
  ggtitle('분식전문점 연매출 TOP10 상권')+
  theme(plot.title = element_text(size=25, face='bold', hjust = 0.5))+
  labs(x="연매출금액",y = "상권")+
  scale_x_continuous(limits=c(0,750000000),labels = tf)+
  theme(legend.position = "none")

ggsave("Machine_visual/Snackbar.png")

#10. 호프-간이주점 연매출 TOP10 상권
Pub <- read.csv("Machine_visual/Pub.csv")

Pub_revenue<-Pub[,1:2]
names(Pub_revenue)[2] <- c('호프_간이주점_연매출_금액')

ggplot(Pub_revenue,aes(x = 호프_간이주점_연매출_금액, y = reorder(상권_코드_명,-호프_간이주점_연매출_금액), fill=상권_코드_명))+
  geom_bar(stat='identity') +
  ggtitle('호프_간이주점 연매출 TOP10 상권')+
  theme(plot.title = element_text(size=25, face='bold', hjust = 0.5))+
  labs(x="연매출금액",y = "상권")+
  scale_x_continuous(limits=c(0,700000000),labels = tf)+
  theme(legend.position = "none")

ggsave("Machine_visual/Pub.png")

#11. 커피_음료 연매출 TOP10 상권
Cafe <- read.csv("Machine_visual/Cafe.csv")

Cafe_revenue<-Cafe[,1:2]
names(Cafe_revenue)[2] <- c('커피_음료_연매출_금액')

ggplot(Cafe_revenue,aes(x = 커피_음료_연매출_금액, y = reorder(상권_코드_명,-커피_음료_연매출_금액), fill=상권_코드_명))+
  geom_bar(stat='identity') +
  ggtitle('커피_음료 연매출 TOP10 상권')+
  theme(plot.title = element_text(size=25, face='bold', hjust = 0.5))+
  labs(x="연매출금액",y = "상권")+
  scale_x_continuous(limits=c(0,750000000),labels = tf)+
  theme(legend.position = "none")

ggsave("Machine_visual/Cafe.png")