import React, { useState } from 'react';
import { View, TextInput, TouchableOpacity, Text, StyleSheet } from 'react-native';

const LoginScreen = ({ navigation }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    // Lógica para procesar el inicio de sesión aquí
    console.log('Username:', username);
    console.log('Password:', password);
    //TODO: Add auth logic
    navigation.navigate('InventoryManager');
  };

  // Verificar si los inputs tienen contenido
  const isButtonDisabled = !username || !password;

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        placeholder="Username"
        value={username}
        onChangeText={setUsername}
        placeholderTextColor="#999999"
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
        placeholderTextColor="#999999"
      />
      <TouchableOpacity
        style={[styles.button, isButtonDisabled && styles.buttonDisabled]}
        onPress={handleLogin}
        disabled={isButtonDisabled}
      >
        <Text style={styles.buttonText}>Login</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 30,
    backgroundColor: '#FFFFFF',
  },
  input: {
    width: '100%',
    height: 50,
    paddingHorizontal: 10,
    marginBottom: 20,
    fontSize: 16,
    color: '#000000',
    borderBottomWidth: 1,
    borderBottomColor: '#DDDDDD',
  },
  button: {
    width: '100%',
    height: 50,
    borderRadius: 25,
    backgroundColor: '#9681EB',
    justifyContent: 'center',
    alignItems: 'center',
  },
  buttonDisabled: {
    backgroundColor: '#999999',
  },
  buttonText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: 'bold',
  },
});

export default LoginScreen;
