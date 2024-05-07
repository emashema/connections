<template>
    <div class="connection" :class="'level-'+connection.level">
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
    }
}
</script>