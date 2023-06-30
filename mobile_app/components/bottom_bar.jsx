import React from 'react';
import { View, StyleSheet } from 'react-native';

const BottomBar = ({ children }) => {
  return (
    <View style={styles.bottomBar}>
      {children}
    </View>
  );
};

const styles = StyleSheet.create({
  bottomBar: {
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
    flexDirection: 'row',
    justifyContent: 'space-around',
    alignItems: 'center',
    height: 55, // Ajusta el valor según el tamaño deseado
    backgroundColor: '#6527BE',
  },
});

export default BottomBar;
