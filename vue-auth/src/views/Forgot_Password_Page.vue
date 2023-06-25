<template>
    <main class="form-signin w-100 m-auto">
        <div v-if="notify.cls" :class="`${notify.cls}`" role="alert">
            {{ notify.message  }}
        </div>

    <form @submit.prevent="submit">
      <h1 class="h3 mb-3 fw-normal">Please Enter Your Email</h1>
  
      <div class="form-floating">
        <input v-model='email' type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
        <label for="floatingInput">Email address</label>
      </div>
  
      <button class="btn btn-primary w-100 py-2 mt-3" type="submit">Submit</button>
    </form>
</main>
</template>

<script lang="ts">
import axios from "axios";
import {reactive, ref} from "vue";

export default {
    setup (){
        const email = ref("");
        const notify = reactive({
            cls: "",
            message: "",
        })

        const submit = async () => {
            const response = await axios.post("forgot", {email: email.value});
            if (response.status === 200){
                notify.cls = "alert alert-success";
                notify.message = "Please check your email for a reset link.";
            }
            else{
                notify.cls = "alert alert-danger";
                notify.message = "Something went wrong. Please try again.";
        }};


        return {
            notify,
            email,
            submit,
        };
    }
}

</script>