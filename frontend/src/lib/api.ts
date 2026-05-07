const BASE_URL = process.env.NEXT_PUBLIC_API_URL;

async function request(endpoint: string, data: any) {
  const res = await fetch(`${BASE_URL}${endpoint}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!res.ok) {
    throw new Error("API request failed");
  }

  return res.json();
}

export async function postProbe(data: any) {
  return request("/api/probe", data);
}

export async function postTraceroute(data: any) {
  return request("/api/traceroute", data);
}

export async function postFullScan(data: any) {
  return request("/api/full-scan", data);
}
