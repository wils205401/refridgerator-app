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
import HomeScreen from "./components/HomeScreen";
import CreateScreen from "./components/CreateScreen";
import RecipeScreen from "./components/RecipeScreen";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import MaterialCommunityIcons from "react-native-vector-icons/MaterialCommunityIcons";

const bottomTab = createBottomTabNavigator();

function MyTabs() {
  return (
    <bottomTab.Navigator
      initialRouteName="HomeScreen"
      screenOptions={{
        tabBarActiveTintColor: "#e91e63",
      }}
    >
      <bottomTab.Screen
        name="CreateScreen"
        component={CreateScreen}
        options={{
          tabBarLabel: "Create",
          tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="plus" color={color} size={size} />
          ),
        }}
      />
      <bottomTab.Screen
        name="HomeScreen"
        component={HomeScreen}
        options={{
          tabBarLabel: "Home",
          tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="home" color={color} size={size} />
          ),
        }}
      />
      <bottomTab.Screen
        name="RecipeScreen"
        component={RecipeScreen}
        options={{
          tabBarLabel: "Recipes",
          tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="food" color={color} size={size} />
          ),
        }}
      />
    </bottomTab.Navigator>
  );
}

const Stack = createNativeStackNavigator();

const App = () => {
  return (
    <NavigationContainer>
      {/* <Stack.Navigator screenOptions={{ headerShown: false }}>
        <Stack.Screen
          name="Home"
          component={HomeScreen}
          // options={{ title: "Loading" }}
        /> */}
      <bottomTab.Navigator screenOptions={{ headerShown: false }}>
        <bottomTab.Screen name="bottom tab" component={MyTabs} />
      </bottomTab.Navigator>
      {/* </Stack.Navigator> */}
    </NavigationContainer>
  );
};

export default App;
