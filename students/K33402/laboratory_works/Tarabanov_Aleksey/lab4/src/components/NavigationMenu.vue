<template>
  <nav>
    <ul>
      <li><router-link to="/">Main Page </router-link></li>
      <li><router-link to="/ingredients">Ingredients </router-link></li>
      <li><router-link to="/recipes">Recipes </router-link></li>
      <li><button @click="logout">Log out</button></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'NavigationMenu',
  methods: {
    logout() {
      console.log('Token before logout:', localStorage.getItem('access_token'));
      localStorage.removeItem('access_token');
      console.log('Token after logout:', localStorage.getItem('access_token'));
      this.$router.push('/login');
    }
  }
}
</script>

<style scoped>

button {
  background-color: #3bbcb8;
  color: #ffffff;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

nav {
  width: 100%;
  background-color: #010636;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1000;
}

nav ul {
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 70px;
}

nav ul li {
  margin: 0 10px;
}
</style>
