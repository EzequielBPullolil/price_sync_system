import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import BottomBar from "../components/bottom_bar"

import { Ionicons } from '@expo/vector-icons';

const InventoryManager = ({ navigation }) => {
  const handleNavigationToSearch = ()=>{
    navigation.navigate('SearchInventory');
  }
  return (
    <View style={styles.container}>
      {/* Contenedor principal */}
      <View style={styles.mainContainer}>
        <Text style={styles.text}>Contenido de la pantalla</Text>
      </View>

      {/* Barra inferior */}
      <BottomBar>
        <TouchableOpacity style={styles.button}>
          <View style={styles.buttonBackground}>
            <Ionicons name="add" size={20} color="#FFFFFF" />
          </View>
        </TouchableOpacity>
        <TouchableOpacity style={styles.button} onPress={handleNavigationToSearch}>
          <View style={styles.buttonBackground}>
            <Ionicons name="search" size={20} color="#FFFFFF" />
          </View>
        </TouchableOpacity>
        <TouchableOpacity style={styles.button}>
          <View style={styles.buttonBackground}>
          <Ionicons name="create" size={20} color="#FFFFFF" />
          </View>
        </TouchableOpacity>
      </BottomBar>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FFFFFF',
  },
  button: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  buttonBackground: {
    backgroundColor: '#45CFDD',
    borderRadius: 20, // Define un valor adecuado para lograr la forma circular
    padding: 10, // Ajusta el valor según el tamaño deseado
  },
  buttonText: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#FFFFFF',
  },
});

export default InventoryManager;
