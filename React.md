### Interaction with useState()
- everytime we use setSomething() to change the state, react will rerender the whole component with the new state.
- Use a state variable when a component needs to “remember” some information between renders.
- different/same component will not share same state. state is fully private and isolated to only the one component.
    ```jsx
    function component() {...}

    function app() {
        return (
            <>
                <component />
                <component />
            </>  
        )
    }
    ```
    - In this case, state in first component wont affect second component at all.
    - Also notice how the app component doesn’t “know” anything about the Component state or even whether it has any. Unlike props, state is fully private to the component declaring it. 
- Hooks can only be called at the top level of the component function

### Render and commit
- component render can be triggered by following 2 reasons:
  - initial render
  - state update or its ancestor's state updated:
    - update the component's state automatically queues a render.
- React renders our components:
  - render is recursive: if the updated component returns some other component, React will render that component next, and if that component also returns something, it will render that component next, and so on. The process will continue until there are no more nested components and React knows exactly what should be displayed on screen.
- React commits changes to the DOM:
  - after rendering(calling) cour components, react will modify the DOM
  - react only commit the part that is different than before to DOM, others stay same. React only changes the DOM nodes if there’s a difference between renders

### State as a Snapshot
**will learn**
- Setting state requests a new render.
- React stores state outside of your component, as if on a shelf.
- When you call useState, React gives you a snapshot of the state for that render.
- why state does not update immediately after you set it.
  - answer: in the current component render, you use current state value's snapshot(substitute the current value into component) to calculate the component, and new state value's snapshot will be used to calculate next component render.
  
  ```jsx
  export default function Counter() {
    const [number, setNumber] = useState(0);
    return (
      <>
        <h1>{number}</h1>
        <button onClick={() => {
          setNumber(number + 1);
          setNumber(number + 1);
          setNumber(number + 1);
        }}>+3</button>
      </>
    )
  }
  ```
  Here is what this button’s click handler tells React to do:

  1. setNumber(number + 1): number is 0 so setNumber(0 + 1).
  React prepares to change number to 1 on the next render.
  2. setNumber(number + 1): number is 0 so setNumber(0 + 1).
  React prepares to change number to 1 on the next render.
  3. setNumber(number + 1): number is 0 so setNumber(0 + 1).
  React prepares to change number to 1 on the next render.

  Even though you called setNumber(number + 1) three times, in this render’s event handler number is always 0, so you set the state to 1 three times. This is why, after your event handler finishes, React re-renders the component with number equal to 1 rather than 3
  
- How event handlers access a "snapshot" of the state


### Queueing a Series of State Updates:
sometimes we need to perform multiple operations on the value before queueing the next render.

**Will learn:**
- What "batching" is and how React uses it to process multiple state updates.
- How to apply several updates to the same state variable in a row.

**React batches state updates:**
- re-render only happens after the whole event handler code is finished running. like a waiter doesn't run to kitchen to  kitchen at the mention of your first dish. instead, they let you finish order, let you make change to it, and even take orders from other people at table.
- This lets me update multiple state variable--even from multiple components--without triggering too many re-renders. But this also means UI wont be updated until after event handler. This is known as **batching**. **but when we meet asynchronous code like await/setTimeOut,we dont wait for them, we re-render right after synchronous part ends. we batch code per tick, before the wait is one tick, after the tick is the other tick.**

**Updaing the same state multiple times before the next render**
- if you would like to update the same state variable multiple times before the next render, instead of passing the next state value like setNumber(number + 1), you can pass a function that calculates the next state based on the previous one in the queue, like setNumber(n => n + 1). 
  ```jsx
  import { useState } from 'react';

  export default function Counter() {
    const [number, setNumber] = useState(0);

    return (
      <>
        <h1>{number}</h1>
        <button onClick={() => {
          setNumber(n => n + 1);
          setNumber(n => n + 1);
          setNumber(n => n + 1);
        }}>+3</button>
      </>
    )
  }
  ```
  Here, n => n + 1 is called an updater function. When you pass it to a state setter:

  React queues this function to be processed after all the other code in the event handler has run.
  During the next render, React goes through the queue and gives you the final updated state
  Here’s how React works through these lines of code while executing the event handler:

  `setNumber(n => n + 1): n => n + 1` is a function. React adds it to a queue.
  `setNumber(n => n + 1): n => n + 1` is a function. React adds it to a queue.
  `setNumber(n => n + 1): n => n + 1` is a function. React adds it to a queue.
  When you call useState during the next render, React goes through the queue. The previous number state was 0, so that’s what React passes to the first updater function as the n argument. Then React takes the return value of your previous updater function and passes it to the next updater as n, and so on:
  ![da](image10.png)

**What happens if you update state after replacing it?**
  ```jsx
      import { useState } from 'react';

      export default function Counter() {
        const [number, setNumber] = useState(0);

        return (
          <>
            <h1>{number}</h1>
            <button onClick={() => {
              setNumber(number + 5);
              setNumber(n => n + 1);
            }}>Increase the number</button>
          </>
        )
      }
  ```
Here is what this event handler tells React to do:
  1. setNumber(number + 5): number is 0, so setNumber(0 + 5). React adds “replace with 5” to its queue
  2. setNumber(n => n + 1): n => n + 1 is an updater function. React adds that function to its queue.
  ![](image11.png)
  
During the next render, React goes through the state queue:\
![](image-12.png)
  
**What happens if you replace state after updating it:**
  ```jsx
    export default function Counter() {
      const [number, setNumber] = useState(0);

      return (
        <>
          <h1>{number}</h1>
          <button onClick={() => {
            setNumber(number + 5);
            setNumber(n => n + 1);
            setNumber(42);
          }}>Increase the number</button>
        </>
      )
    }
  ```
  Here's how React works through these lines of code while executing this event handler:
  1. `setNumber(number + 5)`: number is 0, so setNumber(0 + 5). React adds “replace with 5” to its queue.
  2. `setNumber(n => n + 1)`: n => n + 1 is an updater function. React adds that function to its queue.
  3. `setNumber(42)`: React adds “replace with 42” to its queue.
  
  During the next render, React goes through the state queue:
  ![da](image-13.png)

**Recap:**
- Setting state does not change the variable in the existing render, but it requests a new render.
- React processes state updates after event handlers have finished running. This is called batching.
- To update some state multiple times in one event, you can use setNumber(n => n + 1) updater function.
  
### Updating Objects in State

**will learn**
- How to correctly update an object in React state
- How to update a nested object without mutating it.
- what immutability is, and how not to break it.
- How to make object copying less repetitive with lmmer

**Whats mutation**
- immutable Example: value `setX(5)`. the x state changed from 0 to 5, but the number 0 itself didnt change. Its not possible to make any changes to the built-in primitive values like numbers and booleans in JS. 
- mutation: DONT DO `position.x = 5;`
- Example: `const [position, setPosition] = useState({ x: 0, y: 0 });`
  - Object is mutable. we are able to change the contents of the object isself, this is called **mutation** `position.x = 5;`

**Treat State as ready-only**
- whne trying to update a state, dont mutate it but create a new object and replace the old state with setter function. React has no idea the object has changed if you just mutate it and React does not do anything in response.
- Example:
```jsx
  import { useState } from 'react';

  export default function MovingDot() {
    const [position, setPosition] = useState({
      x: 0,
      y: 0
    });
    return (
      <div
        onPointerMove={e => {
          setPosition({
            x: e.clientX,
            y: e.clientY
          });
        }}
        style={{
          position: 'relative',
          width: '100vw',
          height: '100vh',
        }}>
      </div>
    );
  }

```

- Bad Example:
```JSX
  onPointerMove={e => {
    position.x = e.clientX;
    position.y = e.clientY;
  }}
```

**Copying objects with the spread syntax**
- Good Example:
  ```jsx
    setPerson({
      firstName: e.target.value, // New first name from the input
      lastName: person.lastName,
      email: person.email
    });
  ```
- Excellent Example: You can use the `...` object spread syntax so that you don’t need to copy every property separately.
  ```jsx
    setPerson({
      ...person, // Copy the old fields
      firstName: e.target.value // But override this one
    });
  ```
- Best Example: Using a single event handler for multiple fields.
  ```jsx
    export default function Form() {
      const [person, setPerson] = useState({
        firstName: 'Barbara',
        lastName: 'Hepworth',
        email: 'bhepworth@sculpture.com'
      });

      function handleChange(e) {
        setPerson({
          ...person,
          //  use the [ and ] braces inside your object definition to specify a property with a dynamic name.
          [e.target.name]: e.target.value //"name" is specified in tag
        });
      }

      return (
        <>
          <label>
            First name:
            <input
              name="firstName"
              value={person.firstName}
              onChange={handleChange}
            />
          </label>
          <label>
            Last name:
            <input
              name="lastName"
              value={person.lastName}
              onChange={handleChange}
            />
          </label>
          <label>
            Email:
            <input
              name="email"
              value={person.email}
              onChange={handleChange}
            />
          </label>
          <p>
            {person.firstName}{' '}
            {person.lastName}{' '}
            ({person.email})
          </p>
        </>
      );
    }
  ```
  
**Updating a nested object**
- Example:
  ```jsx
    const [person, setPerson] = useState({
      name: 'Niki de Saint Phalle',
      artwork: {
        title: 'Blue Nana',
        city: 'Hamburg',
        image: 'https://i.imgur.com/Sd1AgUOm.jpg',
      }
    });

    const nextArtwork = { ...person.artwork, city: 'New Delhi' };
    const nextPerson = { ...person, artwork: nextArtwork };
    setPerson(nextPerson);

    // or single function call:
    setPerson({
      ...person, // Copy other fields
      artwork: { // but replace the artwork
        ...person.artwork, // with the same one
        city: 'New Delhi' // but in New Delhi!
      }
    });
  ```

**Write concise update logic with Immer When super nested object**

Immer is a popular library that lets you write using the convenient but mutating syntax and takes care of producing the copies for you. With Immer, the code you write looks like you are “breaking the rules” and mutating an object:

```jsx
  updatePerson(draft => {
    draft.artwork.city = 'Lagos';
  });
```

But unlike a regular mutation, it doesn’t overwrite the past state! A complete example using immer below. replace useState with useImmer

```jsx
  import { useImmer } from 'use-immer';

  export default function Form() {
    const [person, updatePerson] = useImmer({
      name: 'Niki de Saint Phalle',
      artwork: {
        title: 'Blue Nana',
        city: 'Hamburg',
        image: 'https://i.imgur.com/Sd1AgUOm.jpg',
      }
    });

    function handleNameChange(e) {
      updatePerson(draft => {
        draft.name = e.target.value;
      });
    }

    function handleTitleChange(e) {
      updatePerson(draft => {
        draft.artwork.title = e.target.value;
      });
    }

    function handleCityChange(e) {
      updatePerson(draft => {
        draft.artwork.city = e.target.value;
      });
    }

    function handleImageChange(e) {
      updatePerson(draft => {
        draft.artwork.image = e.target.value;
      });
    }

    return (
      <>
        <label>
          Name:
          <input
            value={person.name}
            onChange={handleNameChange}
          />
        </label>
        <label>
          Title:
          <input
            value={person.artwork.title}
            onChange={handleTitleChange}
          />
        </label>
        <label>
          City:
          <input
            value={person.artwork.city}
            onChange={handleCityChange}
          />
        </label>
        <label>
          Image:
          <input
            value={person.artwork.image}
            onChange={handleImageChange}
          />
        </label>
        <p>
          <i>{person.artwork.title}</i>
          {' by '}
          {person.name}
          <br />
          (located in {person.artwork.city})
        </p>
        <img 
          src={person.artwork.image} 
          alt={person.artwork.title}
        />
      </>
    );
  }

```


### Updaing Arrays in State

#### arrays are mutable in JS, same as object, but still should treat them like immutable when stored in state. just like with objects, when you want to update an array stored in state, you need to create a new one(or make a copy of an existing one), and then set state to use the new array.

#### you will learn:
  - How to add, remove, or change items in an array in React state.
  - How to update an object inside of an array.
  - How to make array copying

#### Updating arrays without mutation
  - **you should treat arrays in React state as read-only**, this means you shouldn't reassign items inside an array like `arr[0] = 'bird'`, and you shouldn't use methods mutate array like `push()` and `pop()`
  - Instead, we pass a new array to state set function. i.e. to use non-mutating method like `filter()` and `map()` to create a new array.
  - Here is a reference table of common array operations. when dealing with arrays inside React state, avoid using methods in left column, and prefer methods in right column.
  ![](image12.png)
    - Alternatively, use `Immer` which lets you use both column methods

#### Adding to an array
- `push()` will mutate an array, which you dont want:
  ```jsx
    const [name, setName] = useState('');
    const [artists, setArtists] = useState([]);

    <button onClick={() => {
        artists.push({
          id: nextId++,
          name: name,
        });
    }}>
      Add
    </button>
  ```
- Instead, create a new array which contains the existing items and a new item.The easiest way is to use ... array spread syntax: 
  ```jsx
    setArtists( // Replace the state
      [ // with a new array
        ...artists, // that contains all the old items
        { id: nextId++, name: name } // and one new item at the end
      ]
    );
  ```
- The **array spread syntax** also lets you **prepend** an item by placing it before the original items.
  ```jsx
    setArtists([
      { id: nextId++, name: name },
      ...artists // Put old items at the end
    ]);
  ```
  - In this way, spead can do the job of both `push()` and `unshift() `(adding to the beginning of the array)

#### Removing from an array:
- The easiest way to remove an item from an array is to filter it out by `filter`.
  ```jsx
    <ul>
      {artists.map(artist => (
        <li key={artist.id}>
          {artist.name}{' '}
          <button onClick={() => {
            setArtists(
              artists.filter(a =>
                a.id !== artist.id
              )
            );
          }}>
            Delete
          </button>
        </li>
      ))}
    </ul>
  ```
  - Here, artists.filter(a => a.id !== artist.id) means “create an array that consists of those artists whose IDs are different from artist.id”. Note that filter does not modify the original array.

#### Transforming an array
- If you want to change some or all items of the array, you can use `map()` to create a new array. The function you will pass to `map` can decide what to do with each item, based on its data or its index( or both ).

- In this example, 
  ```jsx
  let initialShapes = [
    { id: 0, type: 'circle', x: 50, y: 100 },
    { id: 1, type: 'square', x: 150, y: 100 },
    { id: 2, type: 'circle', x: 250, y: 100 },
  ];
  
  const [shapes, setShapes] = useState(
    initialShapes
  );

  function handleClick() {
      const nextShapes = shapes.map(shape => {
        if (shape.type === 'square') {
          // No change
          return shape;
        } else {
          // Return a new circle 50px below
          return {
            ...shape, // keep id, type, x the same as before
            y: shape.y + 50,
          };
        }
      });
      // Re-render with the new array
      setShapes(nextShapes);
    }
  ```

#### Replacing items in an array
-  Assignments like arr[0] = 'bird' are mutating the original array, so instead you’ll want to use map for this as well.

```jsx
let initialCounters = [
  0, 0, 0
];

const [counters, setCounters] = useState(
    initialCounters
);

// "index" is the index of the array we wanan replace 
// i is the index when we loop the counter array
function handleIncrementClick(index) {
  const nextCounters = counters.map((c, i) => {
    if (i === index) {
      // Increment the clicked counter
      return c + 1;
    } else {
      // The rest haven't changed
      return c;
    }
  });
  setCounters(nextCounters);
}

```

#### Inserting into an array
- Sometimes, you may want to insert an item at a particular position thats neither at the beginning nor at the end. for this, you can use the `...` array spread syntax together with the `slice()` method. create an array that spreads the slice before the insertion point, then new item, and then the rest of the original array.

```jsx
  let nextId = 3;
  const initialArtists = [
    { id: 0, name: 'Marta Colvin Andrade' },
    { id: 1, name: 'Lamidi Olonade Fakeye'},
    { id: 2, name: 'Louise Nevelson'},
  ];

  const [name, setName] = useState('');
  const [artists, setArtists] = useState(
    initialArtists
  );

  function handleClick() {
    const insertAt = 1; // Could be any index
    const nextArtists = [
      // Items before the insertion point:
      ...artists.slice(0, insertAt),
      // New item:
      { id: nextId++, name: name },
      // Items after the insertion point:
      ...artists.slice(insertAt)
    ];
    setArtists(nextArtists);
    setName('');
  }
```


#### Making other changes to an array
- There are some things you cant do with spread syntax and non-mutating methods like `map()` and `filter()`. for example you may want to `reverse()` and `sort()`, but they are mutating the original array, so they can't be used directly. However, **you can copy the array first and then make changes to it.** 
- Example:
  ```jsx
    function handleClick() {
      const nextList = [...list];
      nextList.reverse();
      setList(nextList);
    }
  ```
  - use [...list] spread syntax to create a copy of the original copy of the original array first. Now that you have a copy, youc an use mutating methods like `nextList.reverse()` or `nextList.sort()`, or even assign items with `nextList[0] = "something"`.
  - However, even if you copy an array, you can't mutate existing items inside of it directly. This is bc copying is **shallow** - the new array will contain the same items as the original one. **So if you modify an object insde the copied array, you are mutating the existing state**. For exmaple, code like this is a problem.
  
  ```jsx
    const nextList = [...list];
    nextList[0].seen = true; // Problem: mutates list[0]
    setList(nextList);
  ```

#### Updating objects inside arrays:
 - Although the myNextList array itself is new, the items themselves are the same as in the original myList array. So changing artwork.seen changes the original artwork item. That artwork item is also in yourList, which causes the bug. Bugs like this can be difficult to think about, but thankfully they disappear if you avoid mutating state.
    ```jsx
      const initialList = [
        { id: 0, title: 'Big Bellies', seen: false },
        { id: 1, title: 'Lunar Landscape', seen: false },
        { id: 2, title: 'Terracotta Army', seen: true },
      ];

      const [myList, setMyList] = useState(initialList);
      const [yourList, setYourList] = useState(
        initialList
      );

      function handleToggleMyList(artworkId, nextSeen) {
        const myNextList = [...myList];
        const artwork = myNextList.find(
          a => a.id === artworkId
        );
        artwork.seen = nextSeen; // problem: mutates an existing item
        setMyList(myNextList);
      }

      function handleToggleYourList(artworkId, nextSeen) {
        const yourNextList = [...yourList];
        const artwork = yourNextList.find(
          a => a.id === artworkId
        );
        artwork.seen = nextSeen; // problem: mutates an existing item
        setYourList(yourNextList);
      }
    ```
- You can use map to substitute an old item with its updated version without mutation.  
  ```jsx
    function handleList(artworkId, nextSeen) {
      setMyList(myList.map(artwork => {
        if (artwork.id === artworkId) {
          // Create a *new* object with changes
          return { ...artwork, seen: nextSeen };
        } else {
          // No changes
          return artwork;
        }
      }))
    }
  ```
#### Write conciese update logic with immer
- Generally, you shouldn’t need to update state more than a couple of levels deep. If your state objects are very deep, you might want to restructure them differently so that they are flat
- If you don’t want to change your state structure, you might prefer to use Immer, which lets you write using the convenient but mutating syntax and takes care of producing the copies for you.
- example:
  ```jsx
    import { useState } from 'react';
    import { useImmer } from 'use-immer';

    let nextId = 3;
    const initialList = [
      { id: 0, title: 'Big Bellies', seen: false },
      { id: 1, title: 'Lunar Landscape', seen: false },
      { id: 2, title: 'Terracotta Army', seen: true },
    ];

    export default function BucketList() {
      const [myList, updateMyList] = useImmer(
        initialList
      );
      const [yourList, updateYourList] = useImmer(
        initialList
      );

      function handleToggleMyList(id, nextSeen) {
        updateMyList(draft => {
          const artwork = draft.find(a =>
            a.id === id
          );
          artwork.seen = nextSeen;
        });
      }

      function handleToggleYourList(artworkId, nextSeen) {
        updateYourList(draft => {
          const artwork = draft.find(a =>
            a.id === artworkId
          );
          artwork.seen = nextSeen;
        });
      }

      return (
        <>
          <h1>Art Bucket List</h1>
          <h2>My list of art to see:</h2>
          <ItemList
            artworks={myList}
            onToggle={handleToggleMyList} />
          <h2>Your list of art to see:</h2>
          <ItemList
            artworks={yourList}
            onToggle={handleToggleYourList} />
        </>
      );
    }

    function ItemList({ artworks, onToggle }) {
      return (
        <ul>
          {artworks.map(artwork => (
            <li key={artwork.id}>
              <label>
                <input
                  type="checkbox"
                  checked={artwork.seen}
                  onChange={e => {
                    onToggle(
                      artwork.id,
                      e.target.checked
                    );
                  }}
                />
                {artwork.title}
              </label>
            </li>
          ))}
        </ul>
      );
    }

  ```
  - This is because you’re not mutating the original state, but you’re mutating a special draft object provided by Immer. Similarly, you can apply mutating methods like push() and pop() to the content of the draft. 
  - Behind the scenes, Immer always constructs the next state from scratch according to the changes that you’ve done to the draft. This keeps your event handlers very concise without ever mutating state.