import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(request: NextRequest) {
  const authToken = request.cookies.get("auth_token")?.value;

  // Define the paths that do not require authentication
  const publicPaths = ["/login"];

  // If the user is trying to access a public path, allow the request
  if (publicPaths.includes(request.nextUrl.pathname)) {
    return NextResponse.next();
  }

  // If there's no auth token, redirect to the login page
  if (!authToken) {
    return NextResponse.redirect(new URL("/login", request.url));
  }

  // If the user is authenticated, allow the request
  return NextResponse.next();
}

// Specify the paths the middleware should run on
export const config = {
  matcher: ["/((?!api|_next/static|_next/image|favicon.ico).*)"],
};
