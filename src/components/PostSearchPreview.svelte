<script lang="ts">
    type Props = {
        slug: string
        title: string
        description: string
        category: string,
        tags: Array<string>
    }
    export let post: Props
    export let isLast: boolean = false
</script>
<div class="post-preview hover:bg-theme-primary">
    <div class="flex-1">
        <h4 class="post-preview__title">
            <a href={`/${post.category}/${post.slug}`} title={post.title}>{post.title} &rarr;</a>
        </h4>
        <p class="post-preview__desc">
            {post.description}
        </p>
        <ul class="tag-list">
            {#each post.tags as tag}
                <a class="tag" href={`/tags/${tag}`} title={tag}>{tag}</a>
            {/each}
        </ul>
    </div>
</div>
{#if !isLast}
    <hr class="my-4 text-theme-dark-secondary"/>
{/if}
<style lang="postcss">
    .post-preview {
        @apply  flex gap-6 text-left;
    }
    .post-preview__title {
        @apply text-lg leading-tight font-semibold text-theme-text-primary mb-2;
    }
    :global(html.dark) .post-preview__title {
        @apply text-theme-dark-text-primary;
    }
    .post-preview__desc {
        @apply text-base text-theme-text-secondary leading-5 line-clamp-2;
    }
    :global(html.dark) .post-preview__desc {
        @apply text-theme-dark-text-secondary;
    }
    .tag-list {
        @apply list-none py-2 flex flex-wrap gap-2;
    }
    .tag {
        @apply inline-block text-xs px-4 py-1 rounded-full text-theme-primary bg-theme-secondary;
    }
    :global(html.dark) .tag {
        @apply text-theme-dark-primary bg-theme-dark-secondary;
    }
</style>
