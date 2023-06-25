<template>
  <header
    class="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom bg-dark p-5"
  >
    <ul class="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0">
      <li><router-link to="/" class="nav-link px-2">Home</router-link></li>
    </ul>

    <div class="col-md-3 text-end" v-if="auth">
      <router-link to="/login" class="btn btn-outline-primary me-2" @click="logout">Log Out</router-link>
    </div>

    <div class="col-md-3 text-end" v-if="!auth">
      <router-link to="/login" class="btn btn-outline-primary me-2">Login</router-link>
      <router-link to="/register" class="btn btn-primary">Register</router-link>
    </div>
  </header>
</template>

<script>
import { computed, onMounted } from "vue";
import axios from "axios";
import { useStore } from "vuex";

export default {
  name: "Nav_bar",
  setup(){

    const store = useStore();
    const auth = computed(() => store.state.auth);

    const logout = async () => {
      await axios.post("logout", {}, {withCredentials: true});
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.setItem("token", "");
      await store.dispatch("setAuth", false);

    };
    return {
      auth,
      logout,
    };
  }
};
</script>
