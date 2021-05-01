import React, { useEffect } from "react";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { HomePage, ChannelList } from "../screens";
import { MaterialIcons, MaterialCommunityIcons } from "@expo/vector-icons";
import { theme } from "../theme";
import { getFocusedRouteNameFromRoute } from "@react-navigation/native";
import { Header, Right, Button, Icon, Title } from "native-base";

const TabIcon = ({ name, focused }) => {
  return (
    <MaterialIcons
      name={name}
      size={26}
      color={focused ? theme.tabBtnActive : theme.tabBtnInactive}
    />
  );
};

const TabIcon2 = ({ name, focused }) => {
  return (
    <MaterialCommunityIcons
      name={name}
      size={26}
      color={focused ? theme.tabBtnActive : theme.tabBtnInactive}
    />
  );
};

const Tab = createBottomTabNavigator();

const Home = ({ navigation, route }) => {
  useEffect(() => {
    const screenName = getFocusedRouteNameFromRoute(route) || "홈";
    navigation.setOptions({
      headerTitle: screenName,
      header: () => (
        <Header
          androidStatusBarColor="black"
          iosBarStyle="light-content"
          style={{
            backgroundColor: "white",
            display: "flex",
            alignItems: "center",
            borderBottomColor: "#ffceae",
            borderBottomWidth: 3,
          }}
        >
          <Title style={{ color: "#a6a6a6", fontSize: 16 }}>
            찾고 싶은 상품을 검색해보세요.
          </Title>
          <Right>
            <Button transparent>
              <Icon name="search" style={{ color: "black" }} />
            </Button>
            <Button transparent>
              <Icon name="heart-outline" style={{ color: "black" }} />
            </Button>
            <MaterialIcons
              name="add"
              size={26}
              style={{ margin: 10 }}
              onPress={() => navigation.navigate("ChannelCreation")}
            />
          </Right>
        </Header>
      ),
    });
  });
  return (
    <Tab.Navigator
      tabBarOptions={{
        labelStyle: {
          color: "black",
          marginBottom: 5,
        },
      }}
    >
      <Tab.Screen
        name="홈"
        component={HomePage}
        options={{
          tabBarIcon: ({ focused }) =>
            TabIcon2({
              name: focused ? "home" : "home-outline",
              focused,
            }),
        }}
      />
      <Tab.Screen
        name="삽니다"
        component={ChannelList}
        options={{
          color: "black",
          tabBarIcon: ({ focused }) =>
            TabIcon2({
              name: focused ? "store" : "store-outline",
              focused,
            }),
        }}
      />
      <Tab.Screen
        name="상품등록"
        component={ChannelList}
        options={{
          tabBarIcon: ({ focused }) =>
            TabIcon({
              name: focused ? "add-circle" : "add-circle-outline",
              focused,
            }),
        }}
      />
      <Tab.Screen
        name="크레딧톡"
        component={ChannelList}
        options={{
          tabBarIcon: ({ focused }) =>
            TabIcon({
              name: focused ? "chat-bubble" : "chat-bubble-outline",
              focused,
            }),
        }}
      />
      <Tab.Screen
        name="마이샵"
        component={ChannelList}
        options={{
          tabBarIcon: ({ focused }) =>
            TabIcon({
              name: focused ? "person" : "person-outline",
              focused,
            }),
        }}
      />
    </Tab.Navigator>
  );
};

export default Home;
