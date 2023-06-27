<template>
    <main class="form-signin w-100 m-auto">

        <form @submit.prevent="submit">
        <h1 class="h3 mb-3 fw-normal">Please Enter Your Authenticator Code</h1>
    
        <div class="form-floating">
            <input v-model='code' type="text" class="form-control" id="floatingInput" placeholder="6 digits code">
            <label for="floatingInput">6 digits Code</label>
        </div>
    
        <button class="btn btn-primary w-100 py-2 mt-3" type="submit">Submit</button>
        </form>

        <img v-if="img" :src="img" alt="QR Code" class="mt-3" />
    </main>
</template>

<script lang="ts">
import { SetupContext, ref } from 'vue';
import axios from 'axios';
import qrcode from 'qrcode';

    export default {
        name : "Authenticator_Form",
        props: ["loginData"],
        emits: ["success"],
        setup(props: {loginData: any}, context: SetupContext){
            const code = ref("");
            const img = ref<string | null>(null)

            if (props.loginData.otpauth_url){
                qrcode.toDataURL(props.loginData.otpauth_url, (err: any, data: any) => {
                    if (err) console.log("Error: ", err);
                    img.value = data;
                })
            }
            const submit = async() => {
                const {data, status} = await axios.post("two-factor",
                {
                    ...props.loginData,
                    code: code.value,
                }, {withCredentials: true});

                const AUTH_TOKEN = `Bearer ${data.token}`
                axios.defaults.headers.common["Authorization"] = AUTH_TOKEN;

                if (AUTH_TOKEN){
                    localStorage.setItem("token", AUTH_TOKEN);
                }

                if (status === 200){
                    context.emit("success", true);
                }
                else{
                    context.emit("success", false);
                }
            }

            return {
                code,
                img,
                submit,
            }
        }
    }
</script>