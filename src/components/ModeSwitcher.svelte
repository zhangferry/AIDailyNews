<script lang="ts">
    import { onMount } from 'svelte'
    import { theme } from '../store/theme'

    type ThemeType = 'dark' | 'light'

    const THEME_DARK: ThemeType =  'dark'
    const THEME_LIGHT: ThemeType =  'light'
    let currTheme: ThemeType = THEME_DARK


    function toggleTheme() {
        currTheme = currTheme === THEME_DARK ? THEME_LIGHT : THEME_DARK
        window.document.documentElement.classList.toggle(THEME_DARK, currTheme === THEME_DARK)
        // Update Storage
        localStorage.setItem('theme', currTheme)
        // Update Store
        theme.set(currTheme)
    }

    onMount(() => {
        if (localStorage.getItem('theme') === THEME_DARK || (!('theme' in localStorage) && window.matchMedia(`(prefers-color-scheme: ${THEME_DARK})`).matches)) {
            window.document.documentElement.classList.add(THEME_DARK)
            currTheme = THEME_DARK
        } else {
            window.document.documentElement.classList.remove(THEME_DARK)
            currTheme = THEME_LIGHT
        }
        // Update Store
        theme.set(currTheme)
    })
</script>
<button on:click={toggleTheme} aria-label={currTheme === THEME_DARK ? '切换到浅色模式' : '切换到深色模式'} title="切换阅读主题">
    <slot theme={currTheme}/>
</button>
