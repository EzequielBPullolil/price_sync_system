import React from 'react';
import { View, Text, StyleSheet , TouchableOpacity} from 'react-native';

const DetailInventory = ({ route }) => {
  // Accede al parámetro ID utilizando route.params
  const { barcode } = route.params;
  const handleEdit = () => {
    // Lógica para editar el producto
  };

  const handleDelete = () => {
    // Lógica para eliminar el producto
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Titulo</Text>
      <Text style={styles.label}>Precio:</Text>
      <Text>price</Text>
      <Text style={styles.label}>Stock:</Text>
      <Text>stock</Text>
      <Text style={styles.label}>Código de Barras:</Text>
      <Text>barcode</Text>
      <Text style={styles.label}>Categoría:</Text>
      <Text>category</Text>
      <View style={styles.buttonContainer}>
      <TouchableOpacity
          style={[styles.button, styles.signupButton]}
          onPress={handleEdit}
        >
          <Text style={styles.buttonText}>Edit</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.button, styles.signupButton]}
          onPress={handleDelete}
        >
          <Text style={styles.buttonText}>Delete</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 16,
  },
  label: {
    fontWeight: 'bold',
    marginTop: 8,
  },
  buttonContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: 16,
  },
});

export default DetailInventory;