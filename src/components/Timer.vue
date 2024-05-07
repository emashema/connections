<template>
    <h1>{{ remaining }}</h1>
</template>

<script>
export default {
    data() {
        return {
            target: null,
            remaining:  null
        }
    },
    mounted() {
        var today = new Date();
        var tomorrow = new Date();
        tomorrow.setDate(tomorrow.getDate() + 1);
        tomorrow.setHours(0,0,0,0);

        var diffMs = (tomorrow - today);
        var minutes = Math.floor((diffMs/1000)/60);
        this.target = new Date().getTime() + ((minutes * 60 ) * 1000)

        setInterval(() => { this.startTimer() }, 1000);
    },
    methods: {
        startTimer() {
            var seconds_left = ((this.target - new Date().getTime()) / 1000);

            if (seconds_left >= 0) {
                let hours = this.pad( parseInt((seconds_left % 86400) / 3600) );
                seconds_left = seconds_left % 3600;
                let minutes = this.pad( parseInt(seconds_left / 60) );
                let seconds = this.pad( parseInt( seconds_left % 60 ) );

                this.remaining = hours + ":" + minutes + ":" + seconds;
            }
        },
        pad(n) {
            return (n < 10 ? '0' : '') + n;
        }
    }
}
</script>