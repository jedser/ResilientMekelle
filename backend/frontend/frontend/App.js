import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

// Main Customer Interface for VISION-Mobility-OS
export default function App() {
  return (
    <View style={styles.container}>
      
      {/* Header Section */}
      <Text style={styles.title}>VISION GREEN HUB</Text>
      <Text style={styles.subtitle}>Mekelle, Tigray</Text>

      {/* Charging Status */}
      <View style={styles.card}>
        <Text style={styles.label}>EV Charger Status:</Text>
        <Text style={styles.statusLive}>AVAILABLE (Solar Powered)</Text>
        <Button title="Reserve Plug Now" onPress={() => reservePlug()} />
      </View>

      {/* Eco-Wash Tracker */}
      <View style={styles.card}>
        <Text style={styles.label}>Water Recycled Today:</Text>
        <Text style={styles.metric}>450 Liters</Text>
      </View>

      {/* Accessibility Mode for PWDs */}
      <Button 
        title="Enable Voice Commands (Accessibility)" 
        color="#F4D03F"
        onPress={() => enableVoiceMode()} 
      />

    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff', alignItems: 'center' },
  title: { fontSize: 24, fontWeight: 'bold', color: '#2E86C1' },
  statusLive: { color: 'green', fontWeight: 'bold' }
});
