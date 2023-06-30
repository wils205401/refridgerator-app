import React from "react";
import { StatusBar } from "expo-status-bar";
import {
  Button,
  StyleSheet,
  Dimensions,
  Text,
  View,
  Alert,
  Image,
  SafeAreaView,
  TouchableHighlight,
  Platform,
} from "react-native";
import logo from "../assets/icon.png";
import { NavigationContainer } from "@react-navigation/native";

const CreateScreen = ({ navigation }) => {
  return (
    <View style={styles.container}>
      <Text>CreateScreen</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "space-bewteen",
    backgroundColor: "#222222",
    alignItems: "center",
    justifyContent: "center",
    width: "100%",
  },
  h1: {
    color: "white",
    fontSize: 40,
  },
  h2: {
    color: "white",
    fontSize: 18,
    marginTop: 8,
  },
  image: {
    width: 300,
    height: 260,
    justifyContent: "center",
  },
  buttonContainer: {
    backgroundColor: "grey",
    borderRadius: 5,
    padding: 8,
    margin: 8,
  },
  topContainer: {
    flex: 2,
    justifyContent: "center",
    alignItems: "center",
  },
  middleContainer: {
    flex: 3,
    justifyContent: "flex-start",
    alignItems: "center",
  },
  bottomContainer: {
    justifyContent: "flex-end",
    width: "90%",
    margin: 20,
    padding: 10,
  },
});

export default CreateScreen;
