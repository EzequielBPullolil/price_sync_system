import React, { useEffect, useRef } from 'react';
import { View, StyleSheet, Dimensions } from 'react-native';
import { BarCodeScanner } from 'expo-barcode-scanner';

const SearchInventoryScreen = ({navigation}) => {
  const cameraRef = useRef(null);

  useEffect(() => {
    requestCameraPermission();
  }, []);

  const requestCameraPermission = async () => {
    const { status } = await BarCodeScanner.requestPermissionsAsync();
    if (status !== 'granted') {
      // Manejo de la denegación de permisos de la cámara
      console.log('Se ha denegado el permiso de la cámara');
    }
  };

  const handleBarCodeScanned = ({ data }) => {
    // Lógica para manejar el código de barras escaneado
    console.log('Código de barras escaneado:', data);
    navigation.navigate('DetailInventory', { barcode: data });

  };

  const { width, height } = Dimensions.get('window');
  const rectWidth = width * 0.6;
  const rectHeight = height * 0.3;

  return (
    <View style={styles.container}>
      <BarCodeScanner
        ref={cameraRef}
        style={StyleSheet.absoluteFillObject}
        onBarCodeScanned={handleBarCodeScanned}
      />
      <View style={styles.rectangleContainer}>
        <View style={[styles.rectangle, { width: rectWidth, height: rectHeight }]} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  rectangleContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  rectangle: {
    borderWidth: 2,
    borderColor: '#FFFFFF',
  },
});

export default SearchInventoryScreen;
