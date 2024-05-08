<template>
    <div
        :class="{'zoom': zoom, 'connection': true, ['level-'+connection.level]: true}"
    >
        <h6 class="text-uppercase mb-0 font-weight-bold">{{ connection.key }}</h6>
        <h6 class="text-uppercase mb-0">{{ connection.values.join(", ") }}</h6>
    </div>
</template>

<script>
export default {
    props: {
        "connection": {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            zoom: false
        }
    },
}
</script>