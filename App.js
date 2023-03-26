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

export default function App() {
  console.log(Dimensions.get("screen"));
  return (
    <SafeAreaView style={styles.container}>
      <View
        style={{
          backgroundColor: "dodgerblue",
          width: "100%",
          height: "30%",
        }}
      ></View>
      <Text>Welcome to Leo</Text>
      <Button
        title="Click Me"
        onPress={() =>
          Alert.prompt("Hello", "How are you?", (text) => console.log(text))
        }
      />
      <StatusBar style="auto" />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
});
