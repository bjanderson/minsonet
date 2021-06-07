showPosts()

function showPosts() {
  const postsDiv = document.querySelector('.posts')
  console.log('postsDiv :>> ', postsDiv)
  postsDiv.innerHTML = ''

  const posts = getPosts()
  const postsToDisplay = posts.map((post) => getPostDisplay(post))
  postsToDisplay.forEach((post) => {
    postsDiv.appendChild(post)
  })
}

function getPosts() {
  const posts = [
    {
      author: 'User One',
      title: 'An Interesting Post',
      content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
      createdAt: new Date('9/1/2021')
    },
    {
      author: 'User Two',
      title: 'Another Interesting Post',
      content: 'Nulla facilisi cras fermentum odio eu feugiat pretium nibh ipsum. Turpis cursus in hac habitasse platea dictumst quisque sagittis. Sed egestas egestas fringilla phasellus. Tincidunt dui ut ornare lectus sit. Sit amet est placerat in egestas erat imperdiet sed euismod. Turpis in eu mi bibendum neque egestas. Integer feugiat scelerisque varius morbi enim nunc faucibus a pellentesque. Ut ornare lectus sit amet est placerat in egestas erat. Ultricies tristique nulla aliquet enim tortor at. Mauris a diam maecenas sed enim ut sem. Odio morbi quis commodo odio aenean sed adipiscing diam donec.',
      createdAt: new Date('9/2/2021')
    }
  ]
  return posts
}

function getPostDisplay(post) {
  // const postDiv = document.createElement('div')
  // postDiv.className = 'post'
  // const titleDiv = document.createElement('div')
  // titleDiv.className = 'post-title'
  // titleDiv.innerText = post.title
  // postDiv.appendChild(titleDiv)

  // const authorDiv = document.createElement('div')
  // authorDiv.className = 'post-author'
  // authorDiv.innerText = `${post.author} - ${post.createdAt.toLocaleDateString()}`
  // postDiv.appendChild(authorDiv)

  // const contentDiv = document.createElement('div')
  // contentDiv.className = 'post-content'
  // contentDiv.innerText = post.content
  // postDiv.appendChild(contentDiv)
  // return postDiv

  const postTemplate = document.querySelector('#posttemplate')
  const clone = postTemplate.content.cloneNode(true)

  const title = clone.querySelector('.post-title')
  title.innerText = post.title

  const authorName = clone.querySelector('.post-author-name')
  authorName.innerText = post.author

  const authorDate = clone.querySelector('.post-author-date')
  authorDate.innerText = post.createdAt.toLocaleDateString()

  const content = clone.querySelector('.post-content')
  content.innerText = post.content

  return clone
}
