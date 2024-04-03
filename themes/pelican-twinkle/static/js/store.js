const Store = {
    theme: {
        value: localStorage.theme || "",
        reducers: {
            setTheme: function (theme) {
                Store.theme.value = theme;
                Store.theme.reducers.applyTheme();
            },
            applyTheme: function () {
                let value = Store.theme.value;

                if (value === "") {
                    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
                        value = "dark";
                    }
                    value = "light";
                }

                localStorage.theme = value;
                document.body.dataset.theme = value;

                Store.theme.observer.notify(value);
            }
        },
        observer: {
            listeners: [],
            addObserver: function (listener) {
                return Store.theme.observer.listeners.push(listener) - 1;
            },
            removeObserver: function (id) {
                Store.theme.observer.listeners.splice(id, 1);
            },
            notify: function (value) {
                for (let listener of Store.theme.observer.listeners) {
                    listener(value);
                }
            }
        }
    },
    offset: {
        value: window.scrollY,
        reducers: {
            setOffset: function (offset) {
                Store.offset.value = offset;
            },
            applyOffset: function () {
                const value = Store.offset.value;
                if (value === 0) {
                    document.body.classList.remove('scrolled')
                } else {
                    document.body.classList.add('scrolled')
                }
            }
        }
    }
}

const Action = {
    toggleTheme: function () {
        if (Store.theme.value === 'light') {
            Store.theme.reducers.setTheme('dark');
        } else {
            Store.theme.reducers.setTheme('light');
        }

        Store.theme.reducers.applyTheme();
    },
    applyTheme: function () {
        Store.theme.reducers.applyTheme();
    },
    changeOffset: function (offset) {
        Store.offset.reducers.setOffset(offset);
        Store.offset.reducers.applyOffset();
    },
    applyOffset: function () {
        Store.offset.reducers.applyOffset();
    }
}