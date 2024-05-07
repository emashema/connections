<template>
    <b-modal
        id="results-modal"
        hide-header
        hide-footer
    >
        <div class="text-center">
            <h2 class="font-weight-bold">{{message}}</h2>
            <p> Connections #{{ id }}</p>
            <b-container class="mini-cell-container">
                <b-row
                    v-for="(attempt, index) in attempts"
                    :key="index"
                    no-gutters
                    class="my-1"
                >
                    <b-col
                        v-for="(item, index) in attempt"
                        :key="index"
                    >
                        <div
                            class="mini-cell"
                            :class="'level-'+item.level"
                        >
                        </div>
                    </b-col>
                </b-row>
            </b-container>
            <h5 class="mt-4">NEXT PUZZLE IN</h5>
            <timer/>
        </div>
    </b-modal>
</template>

<script>
import Timer from './Timer.vue';

export default {
    components: {
        Timer
    },
    props: {
        "message": {
            type: String,
            required: true
        },
        "attempts": {
            type: Array,
            required: true
        }
    },
    computed: {
        id() {
            var now = new Date();
            var start = new Date(now.getFullYear(), 0, 0);
            var diff = now - start;
            var day_of_year = Math.floor(diff / (1000 * 60 * 60 * 24));
            return day_of_year
        }
    }
}
</script>

<style>

</style>