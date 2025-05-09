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
    - In this case, if state in first component wont affect second component at all.
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
- setting state triggers renders:
  - whenever we set a existing state to a new value, react queues a new render -> react re-renders the component according to the new state value.
- Rendering takes a snapshot in time:
  - “Rendering” means that React is calling your component, which is a function. The JSX you return from that function is like a snapshot of the UI in time. Its props, event handlers, and local variables were all calculated using its state at the time of the render.
  