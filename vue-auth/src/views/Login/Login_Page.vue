<template>
  <Login_Form @login-data="setLoginData" v-if="loginData.id ===0"/>
  <Authenticator_Form :login-data="loginData" @success="success" v-if="loginData.id !== 0"/>
</template>

<script lang="ts">
  import Login_Form from "./Login_Form.vue";
  import Authenticator_Form from "./Authenticator_Form.vue";
  import { reactive } from "vue";
  import { useRouter } from "vue-router";
  import { useStore } from "vuex";
    export default {
      name: "Login_Page",
      components: { Login_Form, Authenticator_Form },
      setup(){
        const loginData = reactive({ 
          id: 0,
          secret: "",
          otpauth_url: "",
        });
        const router = useRouter();
        const store = useStore();
        const setLoginData = (data: any) => {
          loginData.id = data.id;

          if (data.secret){
            loginData.secret = data.secret;
            loginData.otpauth_url = data.otpauth_url;
          }
        };
        const success = () => {
            store.dispatch("setAuth", true);
            router.push("/");
          }
          return {
            loginData,
            setLoginData,
            success,
          };
      },

  };
</script>