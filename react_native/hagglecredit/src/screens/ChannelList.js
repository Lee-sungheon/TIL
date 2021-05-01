import React, { useEffect, useState } from "react";
import { FlatList } from "react-native";
import styled from "styled-components/native";
import { MaterialIcons } from "@expo/vector-icons";
// import { DB } from "../firebase";
import moment from "moment";

const getDateOrTime = (ts) => {
  const now = moment().startOf("day");
  const target = moment(ts).startOf("day");
  return moment(ts).format(now.diff(target, "day") > 0 ? "MM/DD" : "HH:mm");
};

const ItemContainer = styled.TouchableOpacity`
  flex-direction: row;
  align-items: center;
  border-bottom-width: 1px;
  border-color: ${({ theme }) => theme.itemBorder};
  padding: 15px 20px;
`;

const ItemTextContainer = styled.View`
  flex: 1;
  flex-direction: column;
`;

const ItemTitle = styled.Text`
  font-size: 20px;
  font-weight: 600;
  color: ${({ theme }) => theme.text};
`;

const ItemDesc = styled.Text`
  font-size: 20px;
  font-weight: 600;
  color: ${({ theme }) => theme.itemDesc};
`;

const ItemTime = styled.Text`
  font-size: 12px;
  color: ${({ theme }) => theme.itemTime};
`;

const ItemIcon = styled(MaterialIcons).attrs(({ theme }) => ({
  name: "keyboard-arrow-right",
  size: 24,
  color: theme.ItemIcon,
}))``;

const Item = React.memo(
  ({ item: { id, title, description, createAt }, onPress }) => {
    return (
      <ItemContainer onPress={() => onPress({ id, title })}>
        <ItemTextContainer>
          <ItemTitle>{title}</ItemTitle>
          <ItemDesc>{description}</ItemDesc>
        </ItemTextContainer>
        <ItemTime>{getDateOrTime(createAt)}</ItemTime>
        <ItemIcon />
      </ItemContainer>
    );
  }
);

const Container = styled.View`
  flex: 1;
  background-color: ${({ theme }) => theme.background};
`;

const ChannelList = ({ navigation }) => {
  const [channels, setChannels] = useState([]);

  useEffect(() => {}, []);

  return (
    <Container>
      <FlatList
        data={channels}
        renderItem={({ item }) => (
          <Item
            item={item}
            onPress={(params) => navigation.navigate("Channel", params)}
          />
        )}
        keyExtractor={(item) => item["id"].toString()}
        windowSize={10}
      />
    </Container>
  );
};

export default ChannelList;
