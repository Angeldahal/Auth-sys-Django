<template>
  <main class="form-signin w-100 m-auto">
    <form @submit.prevent="submit">
      <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

      <div class="form-floating">
        <input
          v-model="data.email"
          type="email"
          class="form-control"
          id="floatingInput"
          placeholder="name@example.com"
        />
        <label for="floatingInput">Email address</label>
      </div>
      <div class="form-floating">
        <input
          v-model="data.password"
          type="password"
          class="form-control"
          id="floatingPassword"
          placeholder="Password"
        />
        <label for="floatingPassword">Password</label>
      </div>
      <div class="mb-3">
        <router-link to="/forgot-password" class="text-decoration-none"
          >Forgot Password?</router-link
        >
      </div>

      <button class="btn btn-primary w-100 py-2" type="submit">Sign in</button>
    </form>
  </main>
</template>

<script lang="ts">
    import { SetupContext, reactive } from "vue";
    import axios from "axios";
        export default {
        name: "Login_Page",
        emits: ["LoginData"],
        setup(props: any, context: SetupContext) {
          const data = reactive({
            email: "",
            password: "",
          });


        const submit = async () => {
          const response = await axios.post("login", data);
          context.emit("loginData", response.data);
        };
        return {
            data,
            submit,
          };
        }
    };
</script>
