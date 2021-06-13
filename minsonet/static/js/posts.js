/**
 * We will mock the posts for now, but we really want to be able to get them from a server.
 * Note: mock basically means just making a fake to temporarily stand in place of the real thing.
 */
const allPosts = [
  {
    author: 'User One',
    title: 'An Interesting Post',
    content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    createdAt: new Date('9/1/2021'),
    likes: 1
  },
  {
    author: 'User Two',
    title: 'Another Interesting Post',
    content: 'Nulla facilisi cras fermentum odio eu feugiat pretium nibh ipsum. Turpis cursus in hac habitasse platea dictumst quisque sagittis. Sed egestas egestas fringilla phasellus. Tincidunt dui ut ornare lectus sit. Sit amet est placerat in egestas erat imperdiet sed euismod. Turpis in eu mi bibendum neque egestas. Integer feugiat scelerisque varius morbi enim nunc faucibus a pellentesque. Ut ornare lectus sit amet est placerat in egestas erat. Ultricies tristique nulla aliquet enim tortor at. Mauris a diam maecenas sed enim ut sem. Odio morbi quis commodo odio aenean sed adipiscing diam donec.',
    createdAt: new Date('9/2/2021'),
    likes: 2
  }
]

showPosts()

/**
 * This function is the main function of this file.
 */
function showPosts() {
  const postsDiv = document.querySelector('.posts')
  console.log('postsDiv :>> ', postsDiv)
  postsDiv.innerHTML = ''

  const posts = getPosts()
  const postsToDisplay = posts.map((post) => getPostDisplayUsingTemplate(post))
  postsToDisplay.forEach((post) => {
    postsDiv.appendChild(post)
  })
}

/**
 * This is a simple function right now, but we can change it to make an api request to get the posts from a server in the future
 */
function getPosts() {
  return allPosts.sort((a, b) => a.createdAt.getTime() - b.createdAt.getTime())
}

/**
 * This function uses a pre-made template that lives in the html document.
 * Using a template is easier to maintain and write css for than using pure JS to create the dom elements.
 */
function getPostDisplayUsingTemplate(post) {
  const postTemplate = document.querySelector('#posttemplate').content.cloneNode(true)

  const title = postTemplate.querySelector('.post-title')
  title.innerText = post.title

  const author = postTemplate.querySelector('.post-author')
  author.innerText = post.author

  const date = postTemplate.querySelector('.post-date')
  date.innerText = post.createdAt.toLocaleDateString()

  const likes = postTemplate.querySelector('.post-likes')
  likes.append(post.likes)

  const content = postTemplate.querySelector('.post-content')
  content.innerText = post.content

  return postTemplate
}

/**
 * This function does basically the same thing as getPostDisplayUsingTemplate,
 * except it does it purely in JavaScript and does not use a pre-made html template.
 */
function getPostDisplayWithoutUsingTemplate(post) {
  const postDiv = document.createElement('div')
  postDiv.className = 'post'
  const titleDiv = document.createElement('div')
  titleDiv.className = 'post-title'
  titleDiv.innerText = post.title
  postDiv.appendChild(titleDiv)

  const postInfoDiv = document.createElement('div')
  postInfoDiv.className = 'post-info'

  const authorSpan = document.createElement('span')
  authorSpan.className = 'post-author'
  authorSpan.innerText = post.author

  const dateSpan = document.createElement('span')
  dateSpan.className = 'post-date'
  dateSpan.innerText = post.createdAt.toLocaleDateString()

  const likesSpan = document.createElement('span')
  likesSpan.className = 'post-likes'
  likesSpan.innerText = `Likes: ${post.likes}`

  postInfoDiv.appendChild(authorSpan)
  postInfoDiv.append(' - ')
  postInfoDiv.appendChild(dateSpan)
  postInfoDiv.append(' - ')
  postInfoDiv.appendChild(likesSpan)

  postDiv.appendChild(postInfoDiv)

  const contentDiv = document.createElement('div')
  contentDiv.className = 'post-content'
  contentDiv.innerText = post.content
  postDiv.appendChild(contentDiv)
  return postDiv
}

document.querySelector('#create_post_button').addEventListener('click', addPost)

function addPost() {
  const title = document.querySelector('#post_title').value
  const content = document.querySelector('#post_content').value
  console.log('title :>> ', title);
  console.log('content :>> ', content);
  allPosts.push({title, content, author: 'Test User', createdAt: new Date(), likes: 0})
  showPosts()
}
