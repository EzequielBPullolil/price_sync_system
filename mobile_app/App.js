import { StyleSheet} from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
//Screens
import HomeScreen from "./screens/home"
import LoginScreen from "./screens/login"
import SignupScreen from "./screens/signup"
import InventoryManager from "./screens/inventory_manager"
import SearchInventory from "./screens/search_inventory"
import DetailInventory from "./screens/detail_inventory"
const Stack = createStackNavigator();
export default function App() {

  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} />

        {/* Auth screens */}
        <Stack.Screen name="Login" component={LoginScreen} />
        <Stack.Screen name="Signup" component={SignupScreen} />
        {/* Inventorys screen */}
        <Stack.Screen name="InventoryManager" component={InventoryManager} />
        <Stack.Screen name="SearchInventory" component={SearchInventory} />
        <Stack.Screen name="DetailInventory" component={DetailInventory} />
        
      </Stack.Navigator>
    </NavigationContainer>
  );

}
