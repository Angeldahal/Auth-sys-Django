<template>
  <main class="form-signin w-100 m-auto">
    <form @submit.prevent="submit">
      <h1 class="h3 mb-3 fw-normal">Please Register</h1>
      <div class="form-floating">
        <input
          v-model="data.first_name"
          class="form-control"
          placeholder="First Name"
        />
        <label>First Name</label>
      </div>
      <div class="form-floating">
        <input
          v-model="data.last_name"
          class="form-control"
          placeholder="Last Name"
        />
        <label>Last Name</label>
      </div>
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
        <input v-model="data.password" type="password" class="form-control" placeholder="Password" />
        <label>Password</label>
      </div>
      <div class="form-floating">
        <input
          v-model="data.confirm_password"
          type="password"
          class="form-control"
          placeholder="Confirm Password"
        />
        <label>Confirm Password</label>
      </div>

      <button class="btn btn-primary w-100 py-2" type="submit">Register</button>
    </form>
  </main>
</template>

<script lang="ts">
import { reactive } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

export default {
  name: "Register_Page",

  setup() {
    const data = reactive({
      first_name: "",
      last_name: "",
      email: "",
      password: "",
      confirm_password: "",
    });
  const router = useRouter();

  const submit = async () => {
    try{
    await axios.post("register", data);

    await router.push("/login")
    }
    catch (error) {
      alert("Email already exists!")
      console.log(error);
    }
  };
    return {
      data,
      submit,
    }
  }
};


</script>
