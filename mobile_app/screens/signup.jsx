import React, { useState } from 'react';
import { View, TextInput, TouchableOpacity, Text, StyleSheet } from 'react-native';
import {Picker} from '@react-native-picker/picker';
const SignupScreen = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState('');

  const handleSignup = () => {
    // Lógica para procesar el registro aquí
    console.log('Username:', username);
    console.log('Password:', password);
    console.log('Role:', role);
    // ...
  };

  // Verificar si todos los inputs tienen contenido
  const isButtonDisabled = !username || !password || !role;

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
      <View style={styles.selectContainer}>
        <Text style={styles.selectLabel}>Role:</Text>
        <View style={styles.selectInput}>
          <Picker
            selectedValue={role}
            onValueChange={(itemValue) => setRole(itemValue)}
            prompt="Select role"
          >
            <Picker.Item label="Employee" value="employee" />
            <Picker.Item label="Admin" value="admin" />
          </Picker>
        </View>
      </View>
      <TouchableOpacity
        style={[styles.button, isButtonDisabled && styles.buttonDisabled]}
        onPress={handleSignup}
        disabled={isButtonDisabled}
      >
        <Text style={styles.buttonText}>Signup</Text>
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
  selectContainer: {
    width: '100%',
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 20,
  },
  selectLabel: {
    flex: 1,
    fontSize: 16,
    color: '#000000',
  },
  selectInput: {
    flex: 2,
    height: 50,
    paddingHorizontal: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#DDDDDD',
    fontSize: 16,
    color: '#000000',
  },
  button: {
    width: '100%',
    height: 50,
    borderRadius: 5,
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

export default SignupScreen;
