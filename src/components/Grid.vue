<template>
    <b-container class="grid">
        <!-- Results modal -->
        <results-modal
            :day_of_year="day_of_year"
            :attempts="attempts"
            :message="finished_message"
        />

        <b-row class="h2 mb-0 font-weight-bold justify-content-center">
            CONNECTIONS
        </b-row>

        <b-row class="mb-3 justify-content-center text-secondary">
            Create four groups of four!
        </b-row>

        <!-- Grid -->
        <b-row no-gutters>

            <!-- Solved -->
            <b-col cols="12"
                style="margin-top: 5px"
                v-for="connection in solved"
                :key="connection.key"
            >
                <row
                    :ref="connection.level"
                    :connection="connection"
                />
            </b-col>
            
            <!-- Unsolved -->
            <b-col cols="3"
                style="margin-top: 5px"
                v-for="item in unsolved"
                :key="item.value"
            >
                <cell
                    :ref="item.value"
                    :value="item.value"
                    :parent="item.key"
                    @toggle="toggle(item)"
                />
            </b-col>

        </b-row>

        <!-- Mistakes -->
        <b-row class="mt-3 justify-content-center">
            Mistakes remaining:
            <div
                v-for="mistake in mistakes_remaining"
                :key="mistake"
                class="mistake ml-2"
            />
        </b-row>

        <!-- Buttons -->
        <b-row class="mt-4 justify-content-center">
            <b-col>
                <b-button
                    pill
                    variant="outline-secondary"
                    class="mr-1"
                    @click="watchForRefresh++"
                > Shuffle </b-button>
                <b-button
                    pill
                    variant="outline-secondary"
                    class="mr-1"
                    @click="selected = []"
                    :disabled="selected.length == 0"
                > Deselect all </b-button>
                <b-button
                    pill
                    variant="outline-secondary"
                    @click="submit()"
                    :disabled="selected.length != 4"
                > Submit </b-button>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
import Cell from './Cell.vue';
import Row from './Row.vue';
import ResultsModal from './ResultsModal.vue';

export default {
    name: 'App',
    components: {
        Cell,
        Row,
        ResultsModal
    },
    data() {
        return {
            watchForRefresh: 0,

            connections: [],
            attempts: [],
            selected: [],
            solved: [],
            mistakes_remaining: null
        }
    },
    computed: {
        day_of_year() {
            var now = new Date();
            var start = new Date(now.getFullYear(), 0, 0);
            var diff = now - start;
            var day_of_year = Math.floor(diff / (1000 * 60 * 60 * 24));
            return day_of_year
        },
        unsolved() {
            this.watchForRefresh;

            let u = []
            this.connections.filter(c => !this.solved.map(x => x.key).includes(c.key)).forEach(c => {
                c.values.forEach(v => {
                    u.push({
                        level: c.level,
                        key: c.key,
                        value: v,
                    })
                })
            })
            u = this.shuffle(u)
            
            return u
        },
        already_guessed() {
            let r = false
            this.attempts.forEach(attempt => {
                if(attempt.map(x => x.value).sort().join(',') == this.selected.map(x => x.value).sort().join(','))
                    r = true
            })
            return r
        },
        one_away() {
            let r = false
            this.selected.forEach(s => {
                if(this.selected.filter(s1 => s1.level == s.level).length == 3) {
                    r = true
                }
            })
            return r
        },
        finished_message() {
            if(this.mistakes_remaining == 4)
                return 'Amazing!';
            if(this.mistakes_remaining == 3)
                return 'Great!';
            if(this.mistakes_remaining == 2)
                return 'Nice!';
            if(this.mistakes_remaining == 1)
                return 'Phew...';
            return 'Next time!';
        }
    },
    created() {
        this.connections = require('./../assets/data/connections/'+this.day_of_year+'.json')

        this.mistakes_remaining = 4
    },
    methods: {
        shuffle(array) {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
            return array
        },
        toggle(item) {
            if(this.selected.includes(item))
                this.selected = this.selected.filter(s => s.value != item.value)
            else if (this.selected.length < 4)
                this.selected.push(item)
        },
        submit() {

            if(this.already_guessed) {
                this.$toast('Already guessed!')
                return;
            }

            // Bounce
            this.selected.forEach((x, i) => {
                setTimeout(() => {
                    this.$refs[x.value][0].bounce = true
                }, (i+1)*200);
            });

            setTimeout(() => {
                // Register attempt
                this.attempts.push(this.selected)
                
                let categories = new Set(this.selected.map(s => s.level))

                // Correct guess
                if(categories.size == 1) {
                    setTimeout(() => {
                        let category = categories.values().next().value
                        this.solved.push(this.connections.find(c => c.level == category))

                        // Zoom
                        setTimeout(() => {
                            this.$refs[category][0].zoom = true
                            setTimeout(() => {
                                this.$refs[category][0].zoom = false
                            }, 550);
                        }, 50);

                        this.selected = []
                    }, 500)
                }
                // Incorrect guess
                else {
                    // Shake
                    this.selected.forEach(x => {
                        this.$refs[x.value][0].shake = true
                        setTimeout(() => {
                            this.$refs[x.value][0].shake = false
                            this.$refs[x.value][0].bounce = false
                        }, 800);
                    });

                    this.mistakes_remaining--;

                    if(this.one_away == true)
                        this.$toast('One away...')
                }

                // Game Over ?
                setTimeout(() => {
                    if(this.unsolved.length == 0 || this.mistakes_remaining == 0) {
                        this.$toast(this.finished_message)
                        setTimeout(() => {
                            this.$bvModal.show('results-modal')
                        }, 1000);
                    }
                }, 1000);

            }, 1000);
        }
    }
}
</script>