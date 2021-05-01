import React, { useState, useEffect } from "react";
import styled from "styled-components/native";
import { Image, TouchableOpacity, View, Dimensions } from "react-native";
import { Content, Card, CardItem, Text } from "native-base";

const PageContainer = styled.ScrollView`
  flex: 1;
`;

const HomeContainer = styled.View`
  margin: 6px;
`;

const HomeText = styled.Text`
  margin: 5px 10px;
  font-size: 16px;
  font-weight: 700;
`;

const HomePage = () => {
  const [idx, setIdx] = useState(0);
  const width = Dimensions.get("window").width;

  useEffect(() => {
    const countdown = setInterval(() => {
      setIdx((idx) => (idx + 1) % 4);
    }, 5000);
    return () => {
      clearInterval(countdown);
    };
  }, []);
  return (
    <PageContainer>
      <TouchableOpacity onPress={() => console.log("banner")}>
        <Image
          source={{
            uri: `${BANNERS[idx]}`,
          }}
          style={{ height: 180, width: "100%" }}
        />
      </TouchableOpacity>
      <HomeContainer>
        <HomeText>오늘의 상품 추천</HomeText>
      </HomeContainer>
      <View
        style={{
          flexDirection: "row",
          flexWrap: "wrap",
          marginRight: 5,
          marginLeft: 5,
        }}
      >
        {ITEMS.map((item) => (
          <TouchableOpacity
            onPress={() => console.log("item")}
            style={{
              width: "50%",
            }}
            keyExtractor={(item) => item["id"].toString()}
          >
            <Content
              style={{
                margin: 5,
              }}
            >
              <Card>
                <CardItem cardBody>
                  <Image
                    source={{
                      uri: `${item.url}`,
                    }}
                    style={{ height: (width - 20) / 2, flex: 1 }}
                  />
                </CardItem>
                <CardItem cardBody>
                  <Text onPress={() => console.log("text")}>{item.title}</Text>
                </CardItem>
              </Card>
            </Content>
          </TouchableOpacity>
        ))}
      </View>
    </PageContainer>
  );
};

export default HomePage;

const BANNERS = [
  "https://media.bunjang.co.kr/images/nocrop/625556674.jpg",
  "https://media.bunjang.co.kr/images/nocrop/626144375.jpg",
  "https://media.bunjang.co.kr/images/nocrop/629785654.jpg",
  "https://media.bunjang.co.kr/images/nocrop/629261066.jpg",
];

const ITEMS = [
  {
    id: 1,
    title: "ITEM1",
    url:
      "http://www.tallykumc.org/xe/files/attach/images/185/869/019/6b03a88b5f273a505efec55236eae5b8.jpg",
    price: 200000,
  },
  {
    id: 2,
    title: "ITEM2",
    url: "https://xenosium.com/wp-content/uploads/1/4212118951.jpg",
    price: 200000,
  },
  {
    id: 3,
    title: "ITEM3",
    url:
      "https://dnvefa72aowie.cloudfront.net/origin/article/202006/d109dc8a07c507dd2de711125af989aaa568cc3eedec778d9537dc98da9c318c.webp?q=95&s=1440x1440&t=inside",
    price: 200000,
  },
  {
    id: 4,
    title: "ITEM4",
    url: "http://www.ant-news.co.kr/news/photo/202008/12237_12920_4942.jpg",
    price: 200000,
  },
  {
    id: 5,
    title: "ITEM5",
    url:
      "https://dnvefa72aowie.cloudfront.net/origin/article/202101/832dfd4dcefea765d27d04e221906c139fd06d1358cacf7b3df46cba0480f5f8.webp?q=95&s=1440x1440&t=inside",
    price: 200000,
  },
  {
    id: 6,
    title: "ITEM1",
    url:
      "http://www.tallykumc.org/xe/files/attach/images/185/869/019/6b03a88b5f273a505efec55236eae5b8.jpg",
    price: 200000,
  },
  {
    id: 7,
    title: "ITEM2",
    url: "https://xenosium.com/wp-content/uploads/1/4212118951.jpg",
    price: 200000,
  },
  {
    id: 8,
    title: "ITEM3",
    url:
      "https://dnvefa72aowie.cloudfront.net/origin/article/202006/d109dc8a07c507dd2de711125af989aaa568cc3eedec778d9537dc98da9c318c.webp?q=95&s=1440x1440&t=inside",
    price: 200000,
  },
  {
    id: 9,
    title: "ITEM4",
    url: "http://www.ant-news.co.kr/news/photo/202008/12237_12920_4942.jpg",
    price: 200000,
  },
  {
    id: 10,
    title: "ITEM5",
    url:
      "https://dnvefa72aowie.cloudfront.net/origin/article/202101/832dfd4dcefea765d27d04e221906c139fd06d1358cacf7b3df46cba0480f5f8.webp?q=95&s=1440x1440&t=inside",
    price: 200000,
  },
];
