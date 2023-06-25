<template>
      <main class="form-signin w-100 m-auto">
    <form @submit.prevent="submit">
      <h1 class="h3 mb-3 fw-normal">Please Reset Your Password</h1>
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

      <button class="btn btn-primary w-100 py-2" type="submit">Submit</button>
    </form>
  </main>
</template>

<script lang="ts">
import axios from 'axios';
import { reactive } from 'vue';
import { useRoute, useRouter } from 'vue-router';

export default {
    name: "Reset_Page",
    setup(){
        const data = reactive({
            password: "",
            confirm_password: "",
        });
        const route = useRoute();
        const router = useRouter();

        const submit = async () => {
            await axios.post('reset', {
                ...data,
                token: route.params.token,
            })
            await router.push('/login')
        }

        return {
            data,
            submit,
        };
    }
}

</script>