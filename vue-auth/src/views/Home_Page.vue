<template>
    <div class="container mt-5">
        <div class="row">
        <div class="col-12">
            <h1>{{ auth? message: "You're not logged in." }}</h1>
        </div>
        </div>
    </div>
</template>

<script lang="ts">
import { ref, onMounted, computed } from "vue";
import axios from "axios";
import { useStore } from "vuex";
export default {
    name: "Home_Page",
    setup(){
        const message = ref("You're not logged in.");
        const store = useStore();
        const auth = computed(() => store.state.auth);
        const AUTH_TOKEN = localStorage.getItem("token");
        if (AUTH_TOKEN) {
            axios.defaults.headers.common["Authorization"] = AUTH_TOKEN;
        }

        onMounted(async () => {
            try {
            const {data} = await axios.get("user");
            message.value = `Welcome ${data.first_name} ${data.last_name}!`;
            await store.dispatch("setAuth", true);
        }
        catch (error) {
            await store.dispatch("setAuth", false);
        }
    });


        return {
            message,
            auth,
        };
    }
};
</script>