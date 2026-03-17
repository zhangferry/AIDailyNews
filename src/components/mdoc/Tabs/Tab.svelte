<script>
	import { getContext } from 'svelte';
	import { TABS } from './Tabs.svelte';

	const tab = {};
	const { registerTab, selectTab, selectedTab } = getContext(TABS);

	registerTab(tab);
</script>

<style>
	button {
        @apply bg-none border-b-2 border-solid border-theme-border m-0 text-theme-text-muted px-4 py-1;
	}
	:global(html.dark) button {
        @apply border-theme-dark-border text-theme-dark-text-muted;
	}

	.selected {
        @apply border-b-2 border-solid border-theme-primary text-theme-primary;
	}
	:global(html.dark) .selected {
        @apply border-theme-dark-primary text-theme-dark-primary;
	}
</style>

<button class:selected="{$selectedTab === tab}" on:click="{() => selectTab(tab)}">
	<slot></slot>
</button>
