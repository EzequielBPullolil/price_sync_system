import React from 'react';
import { View, TouchableOpacity, Text, StyleSheet } from 'react-native';

const HomeScreen = ({ navigation }) => {
  const handleNavigateToLogin = () => {
    navigation.navigate('Login');
  };

  const handleNavigateToSignup = () => {
    navigation.navigate('Signup');
  };

  return (
    <View style={styles.container}>
      <View style={styles.buttonContainer}>
        <TouchableOpacity
          style={[styles.button, styles.loginButton]}
          onPress={handleNavigateToLogin}
        >
          <Text style={styles.buttonText}>Login</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.button, styles.signupButton]}
          onPress={handleNavigateToSignup}
        >
          <Text style={styles.buttonText}>Signup</Text>
        </TouchableOpacity>
      </View>
      <Text style={styles.footerText}>Developed by Ezequiel Karottupullolil</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'flex-start',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingTop: 50,
    backgroundColor: 'white',
  },
  buttonContainer: {
    width: '100%',
    alignItems: 'center',
    marginBottom: 20,
  },
  button: {
    width: '100%',
    height: 50,
    borderRadius: 10,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 10,
  },
  loginButton: {
    backgroundColor: '#6527BE',
  },
  signupButton: {
    backgroundColor: '#45CFDD',
  },
  buttonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: 'bold',
  },
  footerText: {
    color: '#999999',
    fontSize: 14,
    marginTop: 20,
  },
});

export default HomeScreen;
