<template>
    <div class="container mt-5">
        <div class="row">
        <div class="col-12">
            <h1>{{ message }}</h1>
        </div>
        </div>
    </div>
</template>

<script lang="ts">
import { ref, onMounted } from "vue";
import axios from "axios";
export default {
    name: "Home_Page",
    setup(){
        const message = ref("You're not logged in.");
        const AUTH_TOKEN = localStorage.getItem("token");
        if (AUTH_TOKEN) {
            axios.defaults.headers.common["Authorization"] = AUTH_TOKEN;
        }
        onMounted(async () => {

            const {data} = await axios.get("user");
            message.value = `Welcome ${data.first_name} ${data.last_name}!`;
});


        return {
            message,
        };
    }
};
</script>