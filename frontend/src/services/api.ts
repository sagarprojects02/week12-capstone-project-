export const login = async (data: any) => {
  const res = await fetch("http://localhost:8000/login", {
    method: "POST",
    body: JSON.stringify(data),
  });
  return res.json();
};
